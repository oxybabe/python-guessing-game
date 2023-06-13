import random
number = random.randint(1, 10)
guesses_remaining = 3
print("You have 3 attempts to guess the correct number. Good luck!")
while guesses_remaining > 0:
    while True:
        try: 
            guess= int(input("\nGuess any number between 1 and 10: "))
            if 1 <= guess <= 10:
                break
            else: 
                print("Your guess was NOT between the numbers of 1 and 10. Try again.")
        except:
            print("Your guess was not an integer. Try again")
    guesses_remaining -=1
    if guess == number:
            print("You win! You guessed correctly!")
            guesses_remaining = 0
    elif guesses_remaining == 0:
            print("You are out of tries. The correct number was: ", number )
    elif guesses_remaining == 1:
            print("\nSorry, incorrect number!. Try again! You have {} tries remaining.".format(guesses_remaining))
        
     
