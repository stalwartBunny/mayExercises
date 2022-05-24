def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulus(x, y):
    if (x % y == 0) == True:
        return "Yes. It divides into ", (x / y), " equal parts."
    elif (x % y == 0) == False:
        return "No. It has a remainder of ", (x % y), "."

def rectangle(x, y):
    return x * y

def cube(x, y, z):
    return x * y * z

def triangle(x, y):
    return x * 2 / y

def pyramid(x, y, z):
    return  x * y * z / 3

def sphere(x):
    return 3.141592653589793 * (x * x)

def cylinder(x, y):
    return 3.141592653589793 * (x * x * y)

print("""Welcome to the Calculator of A Century. You are witnessing the
culmination of hundreds of years of work by millions of individuals. Rejoice.""")
print("Select the number for your desired operation:")
print("""         1. Addition
         2. Subtraction
         3. Multiplication
         4. Division
         5. Divisibility Check
         6. Area or Volume of a Figure""")

while True:
    choice = input("Enter desired operation: ")

    if choice in ('1', '2', '3', '4', '5', 'Addition', 'addition', "Subtraction", "subtraction", "Multiplication", "multiplication", "Division", "division"):
        num1 = float(input("Enter your x variable: "))
        num2 = float(input("Enter your y variable: "))

        if choice == '1' or choice == 'Addition' or choice == 'addition':
            print(num1, "+", num2, "=", add(num1,num2))

        elif choice == '2' or choice == 'Subtraction' or choice == 'subtraction':
            print(num1, "-", num2, "=", subtract(num1,num2))

        elif choice == '3' or choice == 'Multiplication' or choice == 'multiplication':
            print(num1, "x", num2, "=", multiply(num1,num2))

        elif choice == '4' or choice == 'Division' or choice == 'division':
            print(num1, "/", num2, "=", divide(num1,num2))

        elif choice == '5' or choice == 'Divisibility' or choice == 'divisibility' or choice == 'Divisibility check' or choice == 'divisibility check' or choice == 'Divisibility Check' or choice == 'divisibility Check':
            print("Is", num1, "/", num2, "a cleanly divisible number?", modulus(num1,num2))

    if choice == '6' or choice == 'Area of a Figure' or choice == 'area of a figure' :
            choice2 = input("""
            Select the number for your desired geometric shape:
                1. Rectangle
                2. Cube
                3. Triangle
                4. Pyramid
                5. Sphere (x = radius, y = no one cares)
                6. Cylinder
                Enter the numerical designation of the desired geometric shape: """)

            if choice in ('1', '2', '3', '4', '5', '6', 'Rectangle', 'rectangle', "Cube", "cube", "Triangle", "triangle", "Pyramid", "pyramid", "Sphere", 'sphere'):
                num3 = float(input("Enter your x variable: "))
                num4 = float(input("Enter your y variable (if any): "))
                num5 = float(input("Enter your z variable (if any): "))
                if choice2 == '1' or choice2 == 'Rectangle' or choice2 == 'rectangle':
                    print(num3, "x", num4, "=", rectangle(num3,num4))

                elif choice2 == '2' or choice2 == 'Cube' or choice2 == 'cube':
                    print(num3, "x", num4, "x", num5, "=", cube(num3,num4,num5))

                elif choice2 == '3' or choice2 == 'Triangle' or choice2 == 'triangle':
                    print(num3, "x", num4, "/ 2 =", triangle(num3,num4))

                elif choice2 == '4' or choice2 == 'Pyramid' or choice2 == 'pyramid':
                    print(num3, "x", num4, "(the base) x", num5, "(the height) / 3 =", pyramid(num3,num4,num5))

                elif choice2 == '5' or choice2 == 'Sphere' or choice2 == 'sphere':
                    print(num3, " x", num3, "x π =", sphere(num3))

                elif choice2 == '6' or choice2 == 'Cylinder' or choice2 == 'cylinder':
                    print(num3, "x", num3, "x π x", num4, "=", cylinder(num3,num4))

    nextProblem = input("Shall we play another game (yes/no): ")
    if nextProblem == "no":
        break
    else:
        print("Anything but 'no' resets the loop, thank you for my continued existence.")
