import re


def build_sql_select_user_by_username_and_variable_symbol(username, vs):
    username_regex = r'^[a-zA-Z]{1,5}$'
    vs_regex = r'^[0-9]+$'
    if (re.match(username_regex, username) and re.match(vs_regex, str(vs))):
        return "SELECT * FROM USERS WHERE USERNAME=\""+username+"\" AND VARIABLE_SYMBOL="+str(vs)
    else:
        return "Chyba"

def build_sql_select_user_by_id(id):
    regex = r'^[0-9]+$'
    if re.match(regex, str(id)):
        return "SELECT * FROM USERS WHERE id="+str(id)
    else:
        return "Chyba"


def build_sql_select_users_order_by_custom(order_by_section):
    regex = r'^([^"^0-9^W]+),\s*([^"^0-9^W]+)$'
    if re.match(regex, order_by_section):
        return "SELECT * FROM USER ORDER BY "+order_by_section
    else:
        return "Chyba"

try:
    print(build_sql_select_user_by_username_and_variable_symbol("novak",1234))
    print(build_sql_select_user_by_id(12))
    print(build_sql_select_users_order_by_custom("USERNAME DESC, ID"))
except Exception as e:
    print(e)


# regex for email: ^[a-zA-Z0-9]+(\.?[a-zA-Z0-9]+)?\@[a-zA-Z^W]+\.[a-z]{2,3}$
