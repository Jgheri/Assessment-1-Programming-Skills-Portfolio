#Exercise 8
names = ["Sharelle", "Franco", "Zach", "Aaron", "Yohan", "Aldrin"]
search_name = input("Enter the name you want to search for: ") #asks the user what it wants to search for
if search_name in names: # checks if what it wants to search for is in the list
    print(f"{search_name} was on the list!")
else:
    print(f"{search_name} was not on the list.")
