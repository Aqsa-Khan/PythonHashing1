from hashlib import *
def hashing (make_pass):
    hpass=sha256(make_pass.encode('utf-8')).hexdigest() #pw has been hashed
    #return the hashed password and save it
    return (hpass)

password1="potato"
password2="fightme"
#dictionary for username and password
users = {
        "aqsakhan":password1,                #set users and pw
        "camillesanchez":password2
        }

users["aqsakhan"]=hashing(password1)
users["camillesanchez"]=hashing(password2)

#prompting for existing username
username=input("Username")
#if username is in dictionary:
if username in users:
    password=input("Password")
    #if password is right
    if username in users and users[username] == hashing(password):
        print("Welcome")
    #If password is wrong
    else:
        print("Try again")
        while username in users and users[username]!= password:
            password = input("password")
    
#If username is not in dictionary
else:
    make_username = input ("make username")
    make_pass = input("make password")
    users[make_username]=make_pass
    users[make_pass] = hashing(make_pass)
    
    make_username=input("Username")
    if make_username in users:
        make_pass=input("Password")
        if make_username in users and users[make_username] == hashing(make_pass):
            print("Welcome")

    else:
        print("Try again")
        while make_username in users and users[make_username]!= make_pass:
            make_pass = input("password")

#just to check if it hashes correctly
print(users.items())
