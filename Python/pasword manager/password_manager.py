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
    result = [i for i in storage["password"] if i["website"] == search_web ]
    if result:
        search_user =input("enter your username")
        for i in result:
            if i["user"]==search_user:
                print("your password",i["password"])
            else:
                print("wrong username")
    else:
        print("there is no web like that")
        
    return storage 

def delete(storage):
    delete_web=input("input the web password u want to delete")
    
    exist = any(i["website"] == delete_web for i in storage["password"])
    if exist:
        
        storage["password"] = [i for i in storage["password"] if i["website"] != delete_web]
        print("deleted successfully")
    else:
        print("no website like that")
        
    return storage

def update(storage):
    web=input("the web you want to update")
    
    found = False
    for i in storage["password"]:
        if i["website"] == web:
            found = True
            print("edit the details")
            up_web = input("enter what you want to update (leave blank to skip)").strip().lower()
            up_user = input("enter what you want to update (leave blank to skip)").strip()
            up_password = input("enter what you want to update (leave blank to skip)").strip()
            if up_web:
                i["website"] = up_web
            if up_user:
                i["user"] = up_user
            if up_password:
                i["password"] = up_password
    if not found:
        print("not found")       
    return storage   
 
current_storage = storage
           
while True:
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