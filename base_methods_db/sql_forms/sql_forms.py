class SqlForms:
    select_form = "select {select_object} from {db_name}.{table_name}"
    insert_form = "insert into {db_name}.{table_name} ({column}) values ({values})"
    update_form = "update {db_name}.{table_name} SET {column_name} = '{values}'  where {search_object} {operator} {condition_value}"
    delete_form = "delete from {db_name}.{table_name}  where {search_object} {operator} {condition_value}"
    where_form = " where {search_object} {operator} {condition_value}"
    get_name_columns = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='{db_name}' AND `TABLE_NAME`='{table_name}'"

