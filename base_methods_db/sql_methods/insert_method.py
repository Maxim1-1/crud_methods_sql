from mysql.connector import Error
from base_methods_db.sql_forms.sql_forms import SqlForms
from base_methods_db.sql_connect.sql_connect import DataBaseConnect


class Insert:
    crud_form = SqlForms()

    def __init__(self, name_database, table_name):
        self.name_db = name_database
        self.table_name = table_name
        self.connection = DataBaseConnect().get_inst_connect(database=self.name_db)

    def __get_name_columns(self):
        request = self.crud_form.get_name_columns.format(db_name=self.name_db, table_name=self.table_name)
        cursor = self.connection.cursor()
        cursor.execute(request)
        return cursor.fetchall()

    def insert(self, values):
        try:
            column = [name_column[0] for name_column in self.__get_name_columns()]
            values_for_query = values
            query = self.crud_form.insert_form.format(db_name=self.name_db, table_name=self.table_name,
                                                      column=",".join(column),
                                                      values=",".join(['%s'] * len(column)))

            cursor_inst = self.connection.cursor()
            cursor_inst.executemany(query, values_for_query)
            self.connection.commit()
            print("data successfully added")
            return cursor_inst.fetchall()
        except Error as err:
            print(f"Error: '{err}'")
