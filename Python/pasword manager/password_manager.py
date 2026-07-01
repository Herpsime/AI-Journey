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

def delete(storage):
    delete_web=input("input the web password u want to delete")
    if delete_web in storage["password"]:
        for delete_web in storage["password"]:
            delete={
                "website":delete_web["website"],
                "user":delete_web["user"],
                "password":delete_web["password"]
                    }
        storage["password"].clear(delete)
    else:
        print("no website like that")
        
    return storage

"""def update(storage):
    web=input("the web you want to update")
    up_web = input("enter what you want to update about web if you don't want to update leave a space")
    up_user = input("enter what you want to update about user if you don't want to update leave a space")
    up_password = input("enter what you want to update about password if you don't want to update leave a space")
    updated = {
        "website":up_web,
        "user":up_user,
        "password":up_password
    }
    for i in storage["password"]:
        if i["website"] == web:
            
         return storage  """ 
            
while true:
    choice = int(input("what do you want to do \n 1.add \n 2. search \n 3. delete \n 4. update "))

    match choice:
        case 1:
            current_storage=add(storage)
        case 2:
            current_storage=search(current_storage)
        case 3:
            current_storage=delete(current_storage)
        case 4:
            current_storage=update(current_storage)
        case _:
          print("invalid value")
          
    opt = input("do you want to do it again y/n").lower()
    opt != "y"
    print("exiting password manager system")