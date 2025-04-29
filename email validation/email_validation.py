import re
def emailvalidation(name,email):
     pattern = r"^[a-zA-Z0-9_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
     if name != "" and not name.isnumeric():
        if re.match(pattern,email):
            return True
        else:
            return False
     else:
        return False