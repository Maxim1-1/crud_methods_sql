from base_methods_db.sql_connect.sql_connector import MysqlConnect
from test_project.project_utils.parse_utils import UtilsParse

CREDENTIALS = UtilsParse.parse_credentials()


class DataBaseConnect:

    def get_inst_connect(self, database):
        return MysqlConnect.get_instance(host=CREDENTIALS["host"], password=CREDENTIALS["password"],
                                         user=CREDENTIALS["user"],
                                         database=database)
    @staticmethod
    def close_connect():
        MysqlConnect.close_instance()