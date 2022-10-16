from base_methods_db.crud_methods.crud_methods import CrudMethods
from test_project.project_utils.parse_utils import UtilsParse

CREDENTIALS = UtilsParse.parse_credentials()
CONFIG = UtilsParse.parse_config()
DATA = UtilsParse.parse_test_data()


class TestTable:
    db_name = CREDENTIALS["db_name"]
    table_name = DATA["table_test"]

    def get_last_id(self):
        last_id = self.get_data('id')
        return max(last_id)[0]

    def get_data(self, select_object):
        return CrudMethods(self.db_name, self.table_name).select(select_object)

    def add_data(self, values: list):
        return CrudMethods(self.db_name, self.table_name).insert(values)

    def edit_data(self, column_name, column_values, search_object, condition, operator):
        return CrudMethods(self.db_name, self.table_name).update(column_name, column_values, search_object, condition,
                                                                 operator)

    def delete_data(self, search_object, condition, operator):
        return CrudMethods(self.db_name, self.table_name).delete(search_object, condition, operator)
