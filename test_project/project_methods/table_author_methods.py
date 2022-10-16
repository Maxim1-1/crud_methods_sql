from base_methods_db.crud_methods.crud_methods import CrudMethods
from test_project.project_utils.parse_utils import UtilsParse
from test_project.project_utils.table_utils import TableUtils

CREDENTIALS = UtilsParse.parse_credentials()
CONFIG = UtilsParse.parse_config()
DATA = UtilsParse.parse_test_data()


class AuthorTable:
    db_name = CREDENTIALS["db_name"]
    table_name = DATA["table_author"]

    def __is_validate_id_author_in_table(self, authors, author_id):
        return TableUtils.is_validate_id_in_table(id_in_sql=authors, new_id=author_id)

    def get_data(self, search_object):
        return CrudMethods(self.db_name, self.table_name).select(search_object)

    def add_data(self, values: list):
        if self.__is_validate_id_author_in_table(authors=self.get_data('id'), author_id=(values[0])):
            print('автор с таким id уже существует в таблице, измените id или воспользуйтесь методом update')
        else:
            CrudMethods(self.db_name, self.table_name).insert(values)
            return CrudMethods(self.db_name, self.table_name).insert(values)

    def edit_data(self, column_name, column_values, search_object, condition, operator):
        return CrudMethods(self.db_name, self.table_name).update(column_name, column_values, search_object, condition,
                                                                 operator)

    def delete_data(self, search_object, condition, operator):
        return CrudMethods(self.db_name, self.table_name).delete(search_object, condition, operator)
