from random import randint, choice


def generate_task(level):
    if level == 1:
        num1 = randint(2, 9)
        num2 = randint(2, 9)
        operation = choice(["+", "-", "*"])
        print(num1, operation, num2)

        if operation == "+":
            answer = num1 + num2
        elif operation == "-":
            answer = num1 - num2
        else:
            answer = num1 * num2
        return answer
    else:
        number = randint(11, 29)
        print(number)
        return number ** 2

def get_level():
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        level = input()
        if level in ("1", "2"):
            return int(level)

        print("Incorrect format.")

def get_answer():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Incorrect format.")

def save_result(score, level):
    print("Would you like to save your result to the file? Enter yes or no.")

    answer = input()

    if answer.lower() in ("yes", "y"):
        print("What is your name?")
        name = input()

        if level == 1:
            description = "simple operations with numbers 2-9"
        else:
            description = "integral squares of 11-29"
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(
                f"{name}: {score}/5 in level {level} ({description})\n"
            )
        print('The results are saved in "results.txt".')

def main():
    level = get_level()
    score = 0
    for _ in range(5):
        correct_answer = generate_task(level)
        user_answer = get_answer()
        if user_answer == correct_answer:
            print("Right!")
            score += 1
        else:
            print("Wrong!")
    print(f"Your mark is {score}/5.")
    save_result(score, level)

main()