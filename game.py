import random
choices = ["rock", "paper", "scissors"]
choice = int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors\n"))
if choice <= 2:
    print("you choose\n", choices[choice])
    computer_choice = random.randint(0, 2)
    print("computer choose:\n", choices[computer_choice])
    if choice == 0:
        if computer_choice == 0:
            print("It's draw")
        elif computer_choice == 1:
            print("you loose")
        else:
            print("you win")
    elif choice == 1:
        if computer_choice == 0:
            print("you win")
        elif computer_choice == 1:
            print("It's draw")
        else:
            print("you loose")
    elif choice == 2:
        if computer_choice == 0:
            print("you loose")
        elif computer_choice == 1:
            print("you win")
        else:
            print("It's draw")

else:
    print("you choice is invalid try again")

