import random

num_friends = input("Enter the number of friends joining (including you):\n> ")

try:
    num_friends = int(num_friends)
except ValueError:
    num_friends = 0

if num_friends <= 0:
    print("No one is joining for the party")
else:
    friends = {}
    print("Enter the name of every friend (including you), each on a new line:")

    for _ in range(num_friends):
        name = input("> ")
        friends[name] = 0

    total_amount = float(input("Enter the total amount:\n> "))
    share = round(total_amount / num_friends, 2)

    for name in friends:
        friends[name] = share

    lucky_answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n> ')

    if lucky_answer == "Yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")

        if num_friends > 1:
            new_share = round(total_amount / (num_friends - 1), 2)

            for name in friends:
                if name == lucky_one:
                    friends[name] = 0
                else:
                    friends[name] = new_share
        else:
            friends[lucky_one] = 0

        print(friends)

    else:
        print("No one is going to be lucky")
        print(friends)
