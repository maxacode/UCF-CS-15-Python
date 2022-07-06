"""Lab Objective: Use try and except to handle code errors."""

try:
    num1 = int(input("Please enter a number: "))
    num2 = 0
    div = num1/num2
    print(div)
except ZeroDivisionError:
    print("Cant calculate it")
except ValueError:
    print("Something went wrong!")

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
