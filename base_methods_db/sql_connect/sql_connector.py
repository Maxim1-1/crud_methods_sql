import mysql.connector
from mysql.connector import Error
from test_project.project_utils.parse_utils import UtilsParse

DATA = UtilsParse.parse_config()


class MysqlConnect:
    __instance = None

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        try:

            if MysqlConnect.__instance is None:
                MysqlConnect.__instance = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database,
                    port=3306
                )
            else:
                raise Exception('You cannot create another MySQL connection')

        except Error as error:
            print("connection error ", error)

    @staticmethod
    def get_instance(host, user, password, database):
        if not MysqlConnect.__instance:
            MysqlConnect(host, user, password, database)

        return MysqlConnect.__instance

    @staticmethod
    def close_instance():
        MysqlConnect.__instance.close()

