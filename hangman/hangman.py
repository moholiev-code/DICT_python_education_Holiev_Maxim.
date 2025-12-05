import random

def play_game():
    words = ['python', 'java', 'javascript', 'php']
    secret_word = random.choice(words)

    guessed = ["-" for _ in secret_word]
    used_letters = set()

    mistakes = 0
    max_mistakes = 8

    while mistakes < max_mistakes and "".join(guessed) != secret_word:
        print("".join(guessed))
        letter = input("Input a letter: > ")

        if len(letter) != 1:
            print("You should input a single letter")
            continue

        if not letter.isalpha() or not letter.islower():
            print("Please enter a lowercase English letter")
            continue

        if letter in used_letters:
            print("You've already guessed this letter")
            continue

        used_letters.add(letter)

        if letter in secret_word:
            if letter in guessed:
                print("No improvements")
                mistakes += 1
            else:
                for i in range(len(secret_word)):
                    if secret_word[i] == letter:
                        guessed[i] = letter
        else:
            print("That letter doesn't appear in the word")
            mistakes += 1

    if "".join(guessed) == secret_word:
        print(f"You guessed the word {secret_word}!")
        print("You survived!")
    else:
        print("You lost!")

print("HANGMAN")

while True:
    command = input('Type "play" to play the game, "exit" to quit: > ')
    if command == "play":
        play_game()
    elif command == "exit":
        break
