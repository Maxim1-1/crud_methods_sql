from mysql.connector import Error
from base_methods_db.sql_forms.sql_forms import SqlForms
from base_methods_db.sql_connect.sql_connect import DataBaseConnect


class Select:
    crud_form = SqlForms()

    def __init__(self, name_database, table_name):
        self.name_db = name_database
        self.table_name = table_name
        self.connection = DataBaseConnect().get_inst_connect(database=self.name_db)

    def select(self, select_object, search_object=None, condition=None):
        if select_object == 'all':
            select_object = '*'
        try:
            query = self.crud_form.select_form.format(db_name=self.name_db, table_name=self.table_name,
                                                      select_object=select_object)

            if condition and search_object is not None:
                query = query + self.crud_form.where_form.format(search_object=search_object, condition_value=condition)

            cursor_inst = self.connection.cursor()
            cursor_inst.execute(query)
            return cursor_inst.fetchall()
        except Error as err:
            print(f"Error: '{err}'")
