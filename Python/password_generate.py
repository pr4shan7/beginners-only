# Simple python password generator 
import random                                                               # importing the random module
rand_char= "#$!AaBb12$@^*_&_cC>_dDeEfFgGh09H456786iILKTUVXYZ?)PQrst"
try:                                                                        # exception handling used to display custom error message
    length=input("Enter length of the password you want: ") 
    length=int(length)
    password=""                                                             # used to store random values in it one after another
    for c in range(length):
        password+=random.choice(rand_char)
    print(password)
except ValueError:
    print("You must enter a number not a string12") 
        