#Exercise 3: 
#Asks questions depending on which value is needed
biography = {'Name' : input("Please Put Your First Name: "),#stores the first name that the user types in
             'Second Name' : input("Please Enter Your Second Name: "),#will store the second name that the user types in
             'Hometown' : input("Please Tell Your Hometown: "),#will store the hometown that the user types in
             'Age' : str(input("Please Tell Your Age: "))}#will store the age that the user types in
                    #'str' will make it so that the user can put the age as a string

print("\nFirst Name:",biography['Name'],"\nSecond Name:",biography['Second Name'],"\nHometown:",biography['Hometown'],"\nAge:",biography['Age'])#this prints the output in order and the \ makes it so that it can all be put into one line of code