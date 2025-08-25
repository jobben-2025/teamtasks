##### ND kata: Rock Paper Scissors #####

import random

""" This is a Rock Paper Scissors Game Project
- First You will see the Winning rules of the game.
- After that the game wants that you add your name or even your nickname
  and afterwards you have to choose a Nr. between 1 - 3
- If you choose another Nr for example 4 the game will show you that you have to
  enter a valid Nr.
- And after that you choose a valid Nr. than will your computer choose any random
  Nr. among 1, 2, 3
- After that, it will automaticly determine the winner 
- At the end you can choose also if you want to play again, than you have to enter 'Y' or if you are happy with the result and want to close it, just enter 'N' and you´ll get a thanks message at the end
- Design and create belongs Nedim-34"""

# Print multiline instruction
print("********************************************************")
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:
    print("Enter your name:")
    name = str(input('Your Name please: '))
    print(" ")
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # Take the input from user
    choice = int(input(f"Enter your choice Number {name}: "))

    # Looping until user enters valid input
    while choice > 3 or choice < 1:
            choice = int(input('Enter a valid choice please: '))
            if choice == 1 or choice == 2 or choice == 3:
                break
            else:
                print("Invalid choice, please try again.")
                choice = int(input("Enter your choice Number: "))
            print("Try Again!")

    # Initialize value of choice_name variable corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # Print user choice
    print(f'{name} choice is:', choice_name)
    print()
    print("Now it's Computer's Turn...")

    # Computer chooses randomly any number among 1, 2, and 3
    comp_choice = random.randint(1, 3)

    # Initialize value of comp_choice_name variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name)
    print()
    print(choice_name, 'vs', comp_choice_name)

    # Determine the winner
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = 'Rock'
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = 'Scissors'

    # Print the result
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == choice_name:
        print(f"<== {name} wins! ==>")
    else:
        print("<== Computer wins! ==>")

    # Ask if the user wants to play again
    print(" ")
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'y':
        continue 
    if ans == 'n':
        break
    ans
    
# After coming out of the while loop, print thanks for playing
print(" ")
print(f"Thanks for playing, {name} !")
print("********************************************************")
