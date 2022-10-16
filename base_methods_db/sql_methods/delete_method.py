from mysql.connector import Error
from base_methods_db.sql_forms.sql_forms import SqlForms
from base_methods_db.sql_connect.sql_connect import DataBaseConnect

class Delete:
    crud_form = SqlForms()

    def __init__(self, name_database, table_name):
        self.name_db = name_database
        self.table_name = table_name
        self.connection = DataBaseConnect().get_inst_connect(database=self.name_db)

    def delete(self, search_object, condition, operator):
        try:

            query = self.crud_form.delete_form.format(db_name=self.name_db, table_name=self.table_name,
                                                      search_object=search_object, condition_value=condition,
                                                      operator=operator)
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()

        except Error as err:
            print(f"Error: '{err}'")
