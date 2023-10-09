import re


def build_sql_select_all_from_table(table_name):
    regex = r'^[a-zA-Z]+$'
    if re.match(regex, table_name):
        return "SELECT * FROM " + table_name
    else:
        return "Spatne"


def build_sql_select_custom_from_users(columns):
    regex = r'^[a-zA-Z]+$'
    sql = "SELECT "
    isFirst = True
    for column in columns:
        if(isFirst):
            isFirst = False
            if re.match(regex, column):
                sql += column
            else:
                raise Exception("Nastala chyba")
        elif(re.match(regex, column)):
            sql += ", " + column
        else:
            raise Exception("Nastala chyba")
    sql += " FROM USER"
    return sql


def build_sql_select_users_order_by_custom(order_by_section):
    regex = r'^([^"^0-9^W]+),\s*([^"^0-9^W]+)$'
    if re.match(regex, order_by_section):
        return "SELECT * FROM USER ORDER BY "+order_by_section
    else:
        return "Chyba"

try:
    print(build_sql_select_all_from_table("USER"))
    print(build_sql_select_custom_from_users(["NAME", "USERNAME"]))
    print(build_sql_select_users_order_by_custom("USERNAME DESC, ID"))
except Exception as e:
    print(e)
