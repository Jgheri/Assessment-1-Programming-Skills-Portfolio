#Exercise 5
#stores all the months and the amount of days they have
Calendar = {'Jan': 31,'Feb': 28,'March': 31,'April': 30,'May': 31,'June': 30,
             'July': 31, 'August': 31,'Sept': 30,'Oct': 31,'Nov':30,'Dec':31}
print ("Please pick a month:") #will print the months
for key in Calendar.keys():
    print(key)
month = input("Enter the month: ") # Asks the user to input a month
if month in Calendar:#checks if the month is valid
    print(f"The month of {month} has {Calendar[month]} days.")
else:
    print("Invalid month!")
    
if month == 'Feb' and month in Calendar: #Analyzes and checks if the is a leap year or not
    year = int(input("Enter the year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{month} in {year} has 29 days (leap year).")
    else:
        print(f"{month} in {year} has 28 days.")