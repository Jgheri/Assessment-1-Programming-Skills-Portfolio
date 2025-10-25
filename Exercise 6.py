#Excerise 6
cpw = 12345 #the password
max_attempts = 5 #sets the maximum amount of attempts
attempts = 0

while attempts < max_attempts:#It loops until the maximum amount of tries has been reached 
    password =int(input("Enter in your password: ")) 
    if password == cpw: #Checks if the password is correct
        print ("Correct Password, Welcome User!") #will print if the password is correct
        break #stops the loop from continuing
    else:
        attempts += 1 #will add one more to the users attempts
        current_attempts = max_attempts - attempts #this will check the attempts the user has left
        if current_attempts > 0:
            print (f"Wrong password! You have {current_attempts} left." ) #prints if you still have attempts
        else:
            print ("Maximum amount of attempts has been reached.")#prints if the user ran out of tries