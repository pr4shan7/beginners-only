#Simple python program that tells a number is even or odd
number= int(input("Enter number: "))         #Asking user to enter a number and Type casting
def odd_even(number):                  #Defining function
    if (number%2)==0:                  #Logic
        print(number, "is Even")       
    else:
        print(number, "is Odd")
odd_even(number)                       #Function call
