def cheese_and_crackers(cheeseCount, boxesOfCrackers):
        print(f"You have {cheeseCount} units of cheese and {boxesOfCrackers} boxes of crackers.")
        print("Man, that's enough for a party!")

print("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30)

print("Or we can use variables from a script.")
amountOfCheese = 10
amountOfCrackers = 20

cheese_and_crackers(amountOfCheese, amountOfCrackers)

print("We can even do math inside as well: ")
cheese_and_crackers(10-2*8, 8*2*(-1)+10)
print("Woah, it looks like Python knows PEMDAS!")

print("And we can combine the two, variables and math: ")
cheese_and_crackers(amountOfCheese + 30, amountOfCrackers / 10)
