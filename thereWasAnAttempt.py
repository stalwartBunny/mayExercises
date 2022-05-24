def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x,y):
    return x / y

def modulus(x,y):
    if (x % y == 0) == True:
        return "Yes."
    elif (x % y == 0) == False:
        return "No."



print("""Welcome to the Calculator of A Century. You are witnessing the
culmination of hundreds of years of work by millions of individuals. Rejoice.""")
print("Select the number for your desired operation:")
print("""         1. Addition
         2. Subtraction
         3. Multiplication
         4. Division
         5. Divisibility Check
         6. Area of a Figure""")

while True:
    choice = input("Enter desired operation: ")

    if choice in ('1', '2', '3', '4', '5', '6', 'Addition', 'addition', "Subtraction", "subtraction", "Multiplication", "multiplication", "Division", "division", "Area of a Figure", 'area of a figure'):
        num1 = float(input("Enter your x variable: "))
        num2 = float(input("Enter your y variable: "))

        if choice == '1' or choice == 'Addition' or choice == 'addition':
            print(num1, "+", num2, "=", add(num1,num2))

        elif choice == '2' or choice == 'Subtraction' or choice == 'subtraction':
            print(num1, "+", num2, "=", subtract(num1,num2))

        elif choice == '3' or choice == 'Multiplication' or choice == 'multiplication':
            print(num1, "+", num2, "=", multiply(num1,num2))

        elif choice == '4' or choice == 'Division' or choice == 'division':
            print(num1, "+", num2, "=", divide(num1,num2))

        elif choice == '5' or choice == 'Divisibility' or choice == 'divisibility' or choice == 'Divisibility check' or choice == 'divisibility check' or choice == 'Divisibility Check' or choice == 'divisibility Check':
            print(num1, "+", num2, "=", modulus(num1,num2))

        elif choice == '6' or choice == 'Area of a Figure' or choice == 'area of a figure' :
            print("I'm sorry, this function is not yet complete. Please try another number.")

        nextProblem = input("Shall we play another game (yes/no): ")
        if nextProblem == "no":
            break
        else:
            print("Anything but 'no' resets the loop, thank you for my continued existence.")
