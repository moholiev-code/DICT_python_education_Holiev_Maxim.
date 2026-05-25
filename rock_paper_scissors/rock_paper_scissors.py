import random

print("Enter your name:")
name = input()
print(f"Hello, {name}")
score = 0
try:
    with open("rating.txt", "r") as file:
        for line in file:
            user, rating = line.split()
            if user == name:
                score = int(rating)
except FileNotFoundError:
    pass
options = [
    "rock",
    "gun",
    "lightning",
    "devil",
    "dragon",
    "water",
    "air",
    "paper",
    "sponge",
    "wolf",
    "tree",
    "human",
    "snake",
    "scissors",
    "fire"
]
while True:
    user_choice = input()
    if user_choice == "!exit":
        print("Bye!")
        break
    elif user_choice == "!rating":
        print(f"Your rating: {score}")
    elif user_choice not in options:
        print("Invalid input")
    else:
        computer_choice = random.choice(options)
        if user_choice == computer_choice:
            print(f"There is a draw ({computer_choice})")
            score += 50
        else:
            user_index = options.index(user_choice)
            rotated = (
                options[user_index + 1:]
                + options[:user_index]
            )
            losing_options = rotated[:len(rotated) // 2]
            if computer_choice in losing_options:
                print(
                    f"Sorry, but the computer chose "
                    f"{computer_choice}"
                )
            else:
                print(
                    f"Well done. The computer chose "
                    f"{computer_choice} and failed"
                )
                score += 100