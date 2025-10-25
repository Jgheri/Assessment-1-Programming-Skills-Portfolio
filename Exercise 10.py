#Exercise 10  
def even_or_odd(n):#This functions checks wether or not it is even or odd
    if n % 2 == 0:#it is even when the numbers being divided are 2 and 0
        return f"{n} is even."#prints if the number is even
    else:
        return f"{n} is odd."#prints if the number is odd
def main():#the user should place an input in the function known as main
    try:     
        x = int(input("Please enter a number: "))#this is where the integer should be placed
        print(even_or_odd(x))#it prints out the variable x and wether or not it is even or odd
    except ValueError:#this will alert the user to put the correct data type
        print ("Invalid data type!")#if the data type is incorrect this will print out
if __name__ == "__main__":
    main()