import datetime

name = input('Enter your name: ')
birth_year = input('Enter the year you were born: ')
now = datetime.datetime.now()
current_year = now.year
age = now.year - int(birth_year)
print(f'Hi {name}, you will turn {age} years old this year!')
