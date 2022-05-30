from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, shit Ctrl-C (^C).")
print("If you DO want that, hit return.")

input("? ")

print("opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()

print("I will now ask you for three lines to replace what we have removed.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Now writing these to the file.")
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
target.write(f"{line1} \n{line2} \n{line3}")
print("Closing the file.")
target.close()
