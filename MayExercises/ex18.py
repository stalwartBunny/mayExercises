def printTwo (*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def printTwoAgain (arg1, arg2):
        print(f"arg1: {arg1}, arg2: {arg2}")

def printOne(arg1):
    print(f"arg1: {arg1}")

def printNone():
    print("Hey, there's nothing here!")

printTwo("Yeet", "Beet")
printTwoAgain("Yeet", "Beet")
printOne("Yeet")
printNone()
