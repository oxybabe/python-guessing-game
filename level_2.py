
import random 


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
       
               
                
        
              
        

    