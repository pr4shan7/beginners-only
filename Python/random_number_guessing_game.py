from random import randint  #importing random and randint

h="The number is high"
l="The number is low"

game=True          #initialising game to True



print("   \n  Welcome to GUESSING GAME!!!!")     #defining rules of the game
print("\nRules:\n1.Guess a number.\n2.A number is selected randomly.\n3.If entered number is less than expected number \"The number is high\" is displayed.")
print("4.If entered number is more than expected number\"The number is low\" is displayed.\n     All the best!!!\n")




while game:                   #loop to play if game is true
    guesses=0
    random_number=randint(1,10)                        #choose a random integer
    num=int(input("Guess a number:"))          #input a number
    while random_number!=num:              #condition to find the number
        if random_number>num:
            print(h)
        elif random_number<num:
            print(l)

        num=int(input("Guess a number:"))
        guesses+=1                             #incrementing the number of guesses or turns

    print("Hurray!!! ",num," is the number!!!")
    if guesses<=2:
        print("Awesome!!! you guessed it in only ",guesses," guesses.")
    elif guesses>2 and guesses<=5:
        print("Good!! You guessed it in ",guesses," guesses.")
    elif guesses>5:
        print("Keep going! you guessed it in ",guesses," guesses.")


    bool=input("Do you want to play again:(y/n)")           #input yes or no to play again or not
    while bool!="y" and bool!="n":
        bool=input("Enter only (y/n)")
    if bool=="y":                                           #Continue the game....
        game=True
    elif bool=="n":
        print("Thank you for playing!!!!")                      #exit the game ...
        game=False


