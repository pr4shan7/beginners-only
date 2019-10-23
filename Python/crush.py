#!/usr/bin/env python3

import random
import time

print("We're going to figure out how much your crush likes you using Python3")
print("")

crush_name = input("Please type the name of your crush: ")

print("Crunching numbers to determine how much they like you")

print("- buzzzz -")
time.sleep(3)

print("- wam bang bop -")
time.sleep(1)

# Generating love value 
love_amount = str(random.randint(0, 100)) 

# Return love amount
print(crush_name + " likes you " + love_amount + "%")
