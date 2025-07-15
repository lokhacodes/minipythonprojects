import random

# Initialize scores
player_score = 0
computer_score = 0
max_attempts = 3  # LIMIT: Only 3 guesses allowed!

def guess(x):
    global player_score
    print("🎮 Player Mode - You have 3 attempts to guess the number!")
    random_num = random.randint(1, x)
    guess_num = 0
    attempts = 0

    while guess_num != random_num and attempts < max_attempts:
        guess_num = int(input(f"Attempt {attempts + 1}: Guess a number between 1 and {x}: "))
        attempts += 1
        if guess_num < random_num:
            print("Too low.")
        elif guess_num > random_num:
            print("Too high.")

    if guess_num == random_num:
        print(f"🎉 Congrats! You guessed the number {random_num} correctly in {attempts} tries!")
        player_score += 1
    else:
        print(f"❌ Out of attempts! The number was {random_num}.")

def computer_guess(x):
    global computer_score
    print("💻 Computer Mode - The computer has 3 attempts to guess your number!")
    low = 1
    high = x
    attempts = 0
    feedback = ''

    while feedback != 'c' and attempts < max_attempts:
        if low != high:
            guess_num = random.randint(low, high)
        else:
            guess_num = low
        feedback = input(f"Attempt {attempts + 1}: Is {guess_num} too high (H), too low (L), or correct (C)? ").lower()
        attempts += 1
        if feedback == 'h':
            high = guess_num - 1
        elif feedback == 'l':
            low = guess_num + 1

    if feedback == 'c':
        print(f"🎯 The computer guessed your number {guess_num} correctly in {attempts} tries!")
        computer_score += 1
    else:
        print("❌ The computer failed to guess your number within 3 attempts.")

# Game loop
while True:
    print("\n🎲 Choose a game mode:")
    print("1. You guess the computer's number - Player Mode")
    print("2. The computer guesses your number - Computer Mode")
    print("3. Exit")

    mode = input("Enter 1, 2 or 3: ")

    if mode == '1':
        guess(10)
    elif mode == '2':
        computer_guess(10)
    elif mode == '3':
        print("\n🏁 Final Scores:")
        print(f"🧑 Player Score: {player_score}")
        print(f"🤖 Computer Score: {computer_score}")
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
