import random

WORDS = ["python", "hangman", "computer", "keyboard", "elephant"]
MAX_WRONG_GUESSES = 6

HANGMAN_PICS = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """
]


def choose_word():
    return random.choice(WORDS)


def display_progress(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {MAX_WRONG_GUESSES} incorrect guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word: " + display_progress(word, guessed_letters))
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Incorrect guesses remaining: {MAX_WRONG_GUESSES - wrong_guesses}\n")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word: " + word)
            return

        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    # If loop ends, player has run out of guesses
    print(HANGMAN_PICS[wrong_guesses])
    print(f"Game over! You've run out of guesses. The word was: {word}")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
    print("Thanks for playing Hangman!")


if __name__ == "__main__":
    main()