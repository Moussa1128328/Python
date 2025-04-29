from email_validation import emailvalidation


c=3
while c>0:
    name = input("Enter your name: ")
    email=input("Enter your email: ")
    if emailvalidation(name,email):
        print("Successful")
        break
    else:
        print("Invalid name or email, please try again")
        c-=1
    if c==0:
        print("3 wrong attempts, You have been blocked and reported!")


