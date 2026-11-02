#challenge 1

def clearUsername(username) :
    hasSpace = False
    stripedUsername =username.strip()
    if len(stripedUsername) >= 3 and len(stripedUsername)<= 10 :
        stripedUsername.lower()
        for c in stripedUsername :
            if c == " " :
                hasSpace = True 
                break 
                
        if not hasSpace :
                    
            print(stripedUsername)
        else :
            print("The username has spaces in it , remove the spaces")
    else :
        if len(stripedUsername) > 10:
            
            print(f"The username '{stripedUsername}' is too long.")
        else :
            print(f"username '{stripedUsername}' is too short.") 

   

#username = input ("Enter a username : ")   
#clearUsername(username)


#challenge 2
listOfUsers =[
 { "id": 1, "email": "admin@test.com", "pass": "admin123" },
 { "id": 2, "email": "user@test.com", "pass": "user2024" },
 { "id": 3, "email": "rahal@test.com", "pass": "rahal2024" },
]
def loginUser(email, password) :
    message = {}
    userFound = False
    for user in listOfUsers :
        returnedEmail = user.get("email")
        if returnedEmail == email :
            
            returnedPassword = user.get("pass")
            if returnedPassword == password :
                message.update({"success" : True ,"Token" : "ACCESS_GRANTED" })
                userFound = True
                break
            else :
                message.update({"success" : False ,"error" : "Invalid Credentials" })
                userFound = True
                break

            


    if not userFound :
        message.update({"success" : False ,"error" : "User not found" })
    print(message)

#email = input("Enter Email : ")
#password = input("Enter password : ")

#loginUser(email=email, password= password)

#challeng 3

def transferMoney(userA_Balance , userB_Balance , amount ) :
    message = {}
    if amount > 0 :
        if userA_Balance >= amount :
            userA_Balance -= amount
            userB_Balance += amount
            message.update({"success": True, "newBalanceA": userA_Balance, "newBalanceB":userB_Balance})
        else :
            message.update({"success": False, "error" : "Insufficient funds"})
    else :
        message.update({"success": False, "error" : "Invalid amount"})

    print(message)
#transferMoney(1200, 13, 55)

