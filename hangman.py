import random
import words_list  
import hangman_stages

lives = 6
chosen_word = random.choice(words_list.words)
display = ['_' for _ in chosen_word]
guessed_letters = []  # To keep track of already guessed letters
game_over = False

print("🎯 Welcome to Hangman!")
print(' '.join(display))  # Initial blank word display

while not game_over:
    guess = input("📨 Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in guessed_letters:
        print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
        continue  # Skip rest of the loop

    guessed_letters.append(guess)  # Store the guessed letter

    # Update display if guess is correct
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    # Show updated word progress
    print(' '.join(display))

    # If the guess was incorrect
    if guess not in chosen_word:
        lives -= 1
        print(f"❌ Incorrect! You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print(f"💀 You Lose! The word was '{chosen_word}'.")

    # If there are no blanks left, the user has won
    if '_' not in display:
        game_over = True
        print("🎉 You Win!!")
    # Show hangman visual
    print(hangman_stages.stages[lives])
