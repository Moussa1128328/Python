from Database import authenticate


c=3
while c>0 :

    username=input("enter your username :")
    password=input("enter your password :")
    if authenticate(username,password):
        print(f"welcome {username}!")
        break
    else:
        print("either wrong username or password,please try again")
        c-=1
    if c==0:
        print("you are locked due to 3 failed attempts contact your administrator")
        break








































"""def emailvalidation(email):
    if "@" in email and '.' in email:
        username,domain = email.split("@")
        if username and domain:
            x,y = domain.split(".")
            if x and y:
                return True
    else:
        return False




c=3
while c>0:
    email=input("Enter your email: ")
    if emailvalidation(email):
        print("Successful")
        break
    else:
        print("Invalid email, please try again")
        c-=1"""








