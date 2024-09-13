import random

def choose_word():
    # A list of words for the game
    words = ['python', 'hangman', 'developer', 'programming', 'computer']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\n" + display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        if guess in word:
            guessed_letters.add(guess)
            if set(word) <= guessed_letters:
                print(f"\nCongratulations! You've guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! The letter '{guess}' is not in the word.")
            
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
