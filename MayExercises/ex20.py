from sys import argv

script, inputFile = argv

def print_all(f):
        print(f.read())

def rewind(f):
        f.seek(0)

def print_a_line(line_count, f):
        print(line_count, f.readline())

currentFile = open(inputFile)

print("First let's print the whole file: \n")
print_all(currentFile)

print("Now let's rewind, king of like a vhs tape.")
rewind(currentFile)

print("Printing three lines...")

currentLine = 1
print_a_line(currentLine, currentFile)

currentLine = currentLine + 1
print_a_line(currentLine, currentFile)

currentLine = currentLine + 1
print_a_line(currentLine, currentFile)

#seems like a place for some loops. Give Me the Loops, Brother.
