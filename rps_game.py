import random

# 1. THE BRAIN: Defining how the computer thinks
def play_game():
    options = ['rock', 'paper', 'scissors']
    
    # 2. THE INPUT: Getting data from the human
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(options)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # 3. THE LOGIC: Comparing the choices
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print("You win! Rock smashes scissors.")
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("You win! Paper covers rock.")
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("You win! Scissors cut paper.")    
    else:
        print("The computer wins this time!")

# 4. THE TRIGGER: Actually starting the program
play_game()