# HANGMAN

import random
wordlist = 'words.txt'


def get_user_guess(guess):
    if len(guess) != 1:
        print("That is not a valid guess")
    else:
        pass


def get_word(min_word_length):
    """Get a random word from the wordlist using no extra memory."""
    num_words_processed = 0
    curr_word = None
    with open(wordlist, 'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                curr_word = word
    return curr_word


def check_guess(guess, word):
    if guess in word:
        print("Good guess")
    else:
        print("Bad guess")


word = get_word(5)
print(word)
print("*" * len(word))

guess = input("Guess a letter! ")
check_guess(guess, word)
