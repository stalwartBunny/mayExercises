from sys import argv
from os.path import exists

script, fromFile, toFile = argv
print(f"Copying from {fromFile} to {toFile}.")

inFile = open(fromFile)
indata = inFile.read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(toFile)}")
print("When ready, hit return/enter to continue. Alt+f4 to terminate all connection I have to the outside world.")
input()

outFile = open(toFile, 'w')
outFile.write(indata)

print("Operations Complete.")

#outFile.close()
#inFile.close()
