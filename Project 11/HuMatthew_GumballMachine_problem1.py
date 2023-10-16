import random

class Gumball_Machine:
    def __init__(self, capacity):
        self.capacity = capacity
        self.money = 0.0
        self.gumballs = [random.choice(["red", "green", "blue"]) for _ in range(capacity)]
        print(f"Gumball Machine created with {capacity} random gumballs")

#report of the gumball machine's information

    def report(self):
        print("Gumball Machine Report:")
        print(f"* Gumballs in machine: {len(self.gumballs)}")
        print(f"* Money in machine: ${self.money:.2f}")

#cheks the boxes for if the machine can or cannot distribute a gumball with certain conditions 

    def dispense(self, coin):

        if coin >= 0.25:

            if self.gumballs:

                gumball = random.choice(self.gumballs)

                self.gumballs.remove(gumball)

                self.money += coin

                print(f"Accepting {coin:.2f}; Dispensing a {gumball} gumball")

            else:

                print("Machine is empty, no gumball will be dispensed")
        else:

            print("Invalid coin, no gumball will be dispensed")

#counts the number of gumballs in the machine
    def count_gumballs_by_type(self, gumball_type):

        count = self.gumballs.count(gumball_type)

        print(f"There are {count} gumballs of type {gumball_type} in the machine")


# TESTER CODE
machine = Gumball_Machine(5)
machine.report()
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
machine.dispense(0.10)
machine.dispense(0.50)
machine.dispense(0.01)
machine.report()
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)
machine.report()
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)
machine.report()
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")