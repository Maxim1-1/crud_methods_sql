class TableUtils:
    @staticmethod
    def is_validate_id_in_table(id_in_sql, new_id):
        for id_sql in id_in_sql:
            if id_sql[0] == new_id[0]:
                return True
        else:
            return False