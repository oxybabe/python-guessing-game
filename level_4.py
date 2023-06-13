import random
number = random.randint(1, 10)
player_option = input("Do you want to guess a number or let the computer guess your number? me/computer ") 
if player_option == "me":
     guesses_remaining = 3

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
    
    elif player_option == "computer":
        guesses_remaining = 3
        correct_number = False
              
pick_number = int(input("Pick a number between 1 and 10 for the computer to guess: "))
print(pick_number)
while guesses_remaining > 0 and not correct_number:

        computer_guess = random.randint(1, 10)
        print("Computer guesses...", computer_guess)
        user_input = input("Am I correct? yes/no")
        if user_input == "yes":
             correct_number = True
             print("Computer Wins!")
        elif user_input == "no":
               guesses_remaining = guesses_remaining - 1
               print("Incorrect guess")
        if guesses_remaining == 0:
               print("Computer is out of guesses. You win!")