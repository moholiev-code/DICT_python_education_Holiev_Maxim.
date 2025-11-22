def stage1():
    print(f"Hello! My name is MaxBot.")
    print(f"I was created on 2025.")

def stage2():
    user_name = input("Please enter your name: ")
    print(f"Nice to meet you, {user_name}!")
    return user_name

def stage3(user_name):
    print(f"{user_name}, I will try to guess your age.")
    remainder3 = int(input("Enter the remainder of your age divided by 3: "))
    remainder5 = int(input("Enter the remainder of your age divided by 5: "))
    remainder7 = int(input("Enter the remainder of your age divided by 7: "))
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is: {age} years!")


def stage4():
    number = int(input("Enter any positive number: "))
    print("I can count up to your number:")
    for i in range(number + 1):
        print(i, end=" ")
    print()

def stage5():
    print("Now I will test your programming knowledge.")
    print("Question: Which programming language is used to create this bot?")
    print("1. C++")
    print("2. Python")
    print("3. Java")
    print("4. JavaScript")

    while True:
        answer = input("Your choice (1-4): ")
        if answer == "2":
            print("Correct! Congratulations, you passed the test!")
            break
        else:
            print("Incorrect. Try again.")

def main():
    stage1()
    user_name = stage2()
    stage3(user_name)
    stage4()
    stage5()                # S

if __name__ == "__main__":
    main()
