class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def buy(self):
        choice = input(
            "What do you want to buy? "
            "1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"
        )

        if choice == "back":
            return

        recipes = {
            "1": (250, 0, 16, 4),
            "2": (350, 75, 20, 7),
            "3": (200, 100, 12, 6)
        }

        if choice not in recipes:
            return

        water, milk, beans, price = recipes[choice]

        if self.water < water:
            print("Sorry, not enough water!")
            return

        if self.milk < milk:
            print("Sorry, not enough milk!")
            return

        if self.beans < beans:
            print("Sorry, not enough coffee beans!")
            return

        if self.cups < 1:
            print("Sorry, not enough disposable cups!")
            return

        print("I have enough resources, making you a coffee!")

        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= 1
        self.money += price

    def fill(self):
        self.water += int(
            input("Write how many ml of water do you want to add:\n")
        )
        self.milk += int(
            input("Write how many ml of milk do you want to add:\n")
        )
        self.beans += int(
            input("Write how many grams of coffee beans do you want to add:\n")
        )
        self.cups += int(
            input("Write how many disposable cups do you want to add:\n")
        )

    def take(self):
        print(f"I gave you {self.money}")
        self.money = 0


machine = CoffeeMachine()

while True:
    action = input(
        "Write action (buy, fill, take, remaining, exit):\n"
    )

    if action == "buy":
        machine.buy()

    elif action == "fill":
        machine.fill()

    elif action == "take":
        machine.take()

    elif action == "remaining":
        machine.remaining()

    elif action == "exit":
        break