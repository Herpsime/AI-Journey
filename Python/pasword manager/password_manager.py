storage = {
    "password":[
        {
        "website":"google",
        "user":"arse",
        "password":"1234"
        },
        {
        "website":"youtube",
        "user":"bill",
        "password":"qwer"
        }
    ]
}

def add(storage):
    new_web=input("enter the website")
    new_user=input("enter the user")
    new_password=input("enter the password")
    
    new = {
        "website":new_web,
        "user":new_user,
        "password":new_password
        }
    
    storage["password"].append(new)
    
    return storage

def search(storage):
    search_web=input("input the web u want to search")
    if search_web in storage["password"]:
        search_user =input("enter your username")
        for i in storage["password"]:
            if i["username"]==search_user:
                print("your password",i["password"])
            else:
                print("wrong username")
    else:
        print("there is no web like that")
        
    return storage        