import random

# List of words for the game
words = ['python', 'java', 'computer', 'programming', 'hangman', 'coding']

# Function to randomly choose a word from the list
def choose_word():
    return random.choice(words)

# Function to display the current status of the guessed word
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Hangman game function
def hangman():
    word = choose_word()
    guessed_letters = []  # Store guessed letters
    attempts = 6  # Number of attempts player has
    guessed_word = False
    
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(display_word(word, guessed_letters))

    # Main game loop
    while not guessed_word and attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        # Check if the guess is valid
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You've already guessed '{guess}'. Try again.")
            elif guess in word:
                guessed_letters.append(guess)
                print(f"Good guess! '{guess}' is in the word.")
            else:
                attempts -= 1
                guessed_letters.append(guess)
                print(f"'{guess}' is not in the word. You have {attempts} attempts left.")

        else:
            print("Invalid input. Please guess a single letter.")

        # Display the word with correct guesses
        current_word = display_word(word, guessed_letters)
        print(current_word)

        # Check if the player has guessed the whole word
        if '_' not in current_word:
            guessed_word = True

    if guessed_word:
        print(f"Congratulations! You've guessed the word '{word}'!")
    else:
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")

# Run the game
hangman()
