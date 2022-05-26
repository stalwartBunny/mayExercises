from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

while True:
    somethingImportant = input("Please submit the shadowy secrets of the soul.")
    if somethingImportant == "Mirrors" or somethingImportant == "mirrors":
        print("An unkind word.")
    elif somethingImportant != "Mirrors" or somethingImportant != "mirrors":
        print("These are not your lands.")
    break
