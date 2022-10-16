from test_project.project_methods.table_test_methods import TestTable
from test_project.project_utils.tests_utils import Utils
from test_project.project_utils.add_data_test import UtilsData
from test_project.project_utils.parse_utils import UtilsParse

DATA = UtilsParse.parse_test_data()


def case_two():
    last_id = TestTable().get_last_id()
    tests = TestTable().get_data('all')
    necessary_tests = Utils().get_test_with_equal_id(tests, DATA["count_equal_test"])
    selected_test = UtilsData().add_author_project(necessary_tests, last_id, author=DATA["author_id"],
                                                   project=DATA["project_id"])
    TestTable().add_data(selected_test)
    print('===================== run test =====================')
    TestTable().edit_data(column_name='status_id', column_values=2, search_object='id', operator='>', condition=last_id)
    TestTable().delete_data(search_object='id', condition=last_id, operator=">")


case_two()


