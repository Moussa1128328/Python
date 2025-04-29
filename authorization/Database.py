def authenticate(username,password):
    for i in range(len(l)):
        if username == l[i]["name"] and password == l[i]["pass"]:
            return True

    return False
l=[{"name":"omar","pass":"123"},{"name":"ahmed","pass":"456"},{"name":"alaa","pass":"789"}]