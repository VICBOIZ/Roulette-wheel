def login(users,username,password):
    if username in users and users[username]==password:
        print("Hi ",str(username),"!")
        print("You have logged in!")   
        
    else:
        print("User not found. Please Register.")