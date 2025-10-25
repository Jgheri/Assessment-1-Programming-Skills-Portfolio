#Exercise 4
countries = ["France", "Germany", "Italy", "Spain", "United Kingdom",
             "Portugal", "Netherlands", "Belgium", "Sweden", "Norway"]#both lists are paired up to match each other
capitals = ["Paris", "Berlin", "Rome", "Madrid", "London","Lisbon", "Amsterdam", "Brussels", "Stockholm", "Oslo"]

for i in range(len(countries)): #Creates a loop in which it will keep on looping until the data stored in the variable is finished
    a = input(f"What is the capital of {countries[i]}? ").strip()
    if a.lower() == capitals[i].lower():#this line of code makes it so that it doesnt matter if its capetalized
        print("The answer you have provided is correct!")#This lets you know that the answer the user has types is correct
    else:
        print(f"The answer you have provided is wrong! The capital of {countries[i]} is {capitals[i]}.")#This says if the user has failed to give the correct answer