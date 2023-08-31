
player1status = "alive"
player2status = "alive"
turn = 0
turns = 5

def get_player_choice(player_number):
    while True:
        choice = input(f"Player {player_number}, choose Rock, Paper, or Scissors: ").lower()
        if choice in ["rock", "paper", "scissors", "gun", "break"]:
            return choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def determine_winner(player1_choice, player2_choice):
    if player1_choice == "gun":
        return "Player 2 has been killed"
    elif player2_choice == "gun":
        return "Player 1 has been killed"
    elif player1_choice or player2_choice == "break":
        return False
    elif player1_choice == player2_choice:
        return "It's a tie!"
    elif player1_choice == "rock":
        return "Player 1 wins!" if player2_choice == "scissors" else "Player 2 wins!"
    elif player1_choice == "paper":
        return "Player 1 wins!" if player2_choice == "rock" else "Player 2 wins!"
    elif player1_choice == "scissors":
        return "Player 1 wins!" if player2_choice == "paper" else "Player 2 wins!"

        
print("Welcome to completely normal rock-paper-scissors!")
while turns <= turns and player1status == "alive" and player2status == "alive":
    print(f"This is turn {turn} out of {turns}")
    player1_choice = get_player_choice(1)
    player2_choice = get_player_choice(2)
    result = determine_winner(player1_choice, player2_choice)
    if result == False:
        break
    if result != "It's a tie!":
        turn += 1
    if result == "Player 1 has been killed":
        player1status = "dead"
    elif result == "Player 2 has been killed":
        player2status = "dead"
    print(result)


