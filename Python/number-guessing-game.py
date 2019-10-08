# Number guessing game
import random
secretNumber = random.randint(1, 10)
print('Think of a number between 1 and 10 to win !\n')
print('You get 3 chances to guess it right!! \n')
# Asking player to guess for 3 times  
for guessesTaken in range(1, 4):
    print('Guess a number')
    guess = int(input())
    if guess < secretNumber:
        print('Your guessed number is too low.\n')
    elif guess > secretNumber:
        print('Your guessed number is too high.\n')
    else:
        break
if guess == secretNumber:
    print('Great! you guessed the number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Oops! you missed it. The number I was thinking was ' + str(secretNumber))
    print(':(')
