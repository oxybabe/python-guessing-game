
import random 
count_guesses = 0
correct_number = False
              
pick_number = int(input("Pick a number between 1 and 10 for the computer to guess: "))
print(pick_number)

while not correct_number:
        count_guesses += 1
        computer_guess = random.randint(1, 10)
        print("Computer guesses...", computer_guess)
        user_input = input("Am I high, low, or correct? ")
        if user_input == "correct":
            correct_number = True
            print("Computer Wins!")
        elif user_input == "high":
               print("Incorrect guess is too high.")
        elif user_input == "low":
               print("Incorrect guess is too low.")
        print("Number of guesses: ", count_guesses)