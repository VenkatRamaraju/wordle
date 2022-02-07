#!/usr/bin/env python3

import random


def play(final_word):
    guesses = 6

    while guesses > 0:
        print(guesses, "guesses remaining.")
        guess = input("Enter your guess: ")

        if guess == final_word:
            print()
            print("Correct! You win!")
            return

        if len(guess) < 5:
            continue

        # Actual game logic
        correct_positions = {}

        for i in range(0, 5):
            if guess[i] == final_word[i]:
                correct_positions[i+1] = guess[i]
            elif guess[i] in list(final_word) and guess[i] not in correct_positions.values():
                print(guess[i], "at position", i+1, "is in the word at a different position")
            else:
                print("This word does not have the letter", guess[i], "in its remaining available positions")

        print("Correct positions:", correct_positions)
        print()
        guesses -= 1

    print("Game over. The word was ", final_word)


def main():
    print()
    print("Let's play!")
    print()

    # The word file was taken from: https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt
    with open("5-letter-words.txt", "r") as file:
        data = file.read()
        words = data.split()

    play(words[random.randint(0, len(words)-1)])


if __name__ == "__main__":
    main()
