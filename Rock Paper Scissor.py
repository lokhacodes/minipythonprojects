
import random



def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

def play_round():
    user = input("Choose: 'r' for  Rock, 'p' for  Paper, 's' for  Scissors: ").lower()
    while user not in ['r', 'p', 's']:
        user = input("Invalid input. Please enter 'r', 'p', or 's': ").lower()

    computer = random.choice(['r', 'p', 's'])

    

    if user == computer:
        print("It's a tie!")
        return 'tie'
    elif is_win(user, computer):
        print("You win this round!")
        return 'player'
    else:
        print("Computer wins this round!")
        return 'computer'

def game():
    player_score = 0
    computer_score = 0
    rounds = 3

    print("\n🎮 Welcome to Rock-Paper-Scissors!")
    print("🏁 Best of 3 rounds begins!\n")

    for round_num in range(1, rounds + 1):
        print(f"\n🔢 Round {round_num} of {rounds}")
        result = play_round()

        if result == 'player':
            player_score += 1
        elif result == 'computer':
            computer_score += 1

        # Round result summary
        print(f"Score after Round {round_num}: You: {player_score} | Computer: {computer_score}")

    # Final result summary
    print("\nFinal Result:")
    if player_score > computer_score:
        print("🏆 You won the game!")
    elif player_score < computer_score:
        print("🤖 Computer won the game!")
    else:
        print("🤝 It's a draw!")

# Loop to replay the game
while True:
    game()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != 'y':
        print("👋 Thanks for playing! Goodbye!")
        break
