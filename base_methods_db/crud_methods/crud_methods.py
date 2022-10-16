from base_methods_db.sql_methods.delete_method import Delete
from base_methods_db.sql_methods.select_method import Select
from base_methods_db.sql_methods.insert_method import Insert
from base_methods_db.sql_methods.update_method import Update


class CrudMethods:

    def __init__(self, name_database, table_name):
        self.name_db = name_database
        self.table_name = table_name

    def select(self, select_object, search_object=None, condition=None):
        return Select(name_database=self.name_db, table_name=self.table_name).select(select_object,
                                                                                     search_object=search_object,
                                                                                     condition=condition)

    def insert(self, values):
        return Insert(name_database=self.name_db, table_name=self.table_name).insert(values)

    def update(self, column_name, column_values, search_object, condition, operator):
        return Update(name_database=self.name_db, table_name=self.table_name).update(column_name, column_values,
                                                                                     search_object, condition, operator)

    def delete(self, search_object, condition, operator):
        return Delete(name_database=self.name_db, table_name=self.table_name).delete(search_object, condition, operator)
