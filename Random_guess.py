import random
randomnumber= random.randint(-100,100)
userGuess= None #we dont want the user's input to be illegal like -ve number or something
no_of_guess = 0
while userGuess!= randomnumber:
    userGuess = int(input("Guess a number between -100 and 100: "))
    no_of_guess +=1
    if userGuess == randomnumber:
        print("Your guess is Right")
    else:
        if (userGuess>randomnumber):
            print("Your guess is too high")
        else:
            print("Your guess is too low")
print(f"You guessed the correct number in {no_of_guess} guesses")