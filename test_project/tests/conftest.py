from datetime import datetime
from test_project.project_methods.table_project_methods import ProjectTable
from test_project.project_methods.table_author_methods import AuthorTable
from test_project.project_methods.table_test_methods import TestTable
from test_project.project_utils.parse_utils import UtilsParse
from test_project.project_utils.tests_utils import Utils
from base_methods_db.sql_connect.sql_connect import DataBaseConnect
import pytest

CREDENTIALS = UtilsParse.parse_credentials()
CONFIG = UtilsParse.parse_config()
DATA = UtilsParse.parse_test_data()


@pytest.fixture()
def write_result_test_in_db(request):
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ProjectTable().add_data([(DATA["project_id"], CONFIG["name_project"])])
    AuthorTable().add_data([(DATA["author_id"], CREDENTIALS["user"], DATA["login"], DATA["email"])])
    tests_failed_before = request.session.testsfailed
    yield
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tests_failed = request.session.testsfailed - tests_failed_before
    test_result = Utils().convert_result_test_in_number(tests_failed)
    browser = CONFIG["browser_name"]
    env = DATA["env"]
    session_id = DATA["session_id"]
    project_id = DATA["project_id"]
    method_name = request.node.originalname
    id_new_row = TestTable().get_last_id() + 1
    test_name = f'description for {method_name}'
    TestTable().add_data(
        [(id_new_row, test_name, test_result, method_name, project_id, session_id, start_time, end_time,
          env, browser, DATA["author_id"])])

@pytest.fixture(scope="session")
def close_connect():
    yield
    DataBaseConnect.close_connect()

