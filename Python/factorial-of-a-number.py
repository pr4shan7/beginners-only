number = int(input("Enter Number : "))
def factorial(num):
    fac = 1
    while num > 0:
        fac *= num
        num = num - 1
    return fac

print("Factorial of {} = {}".format(number, factorial(number)))