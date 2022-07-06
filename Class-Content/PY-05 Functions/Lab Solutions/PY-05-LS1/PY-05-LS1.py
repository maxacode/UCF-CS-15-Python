"""Lab Objective: Create a function to handle calculation operations."""
first_num = int(input("Please enter the first number: "))
second_num = int(input("Please enter the second number: "))
operator = input("Please enter one of the following parameters: +, -, *, / :")

def add(num1, num2):
    description = "{} + {} ".format(num1, num2)
    return "The result of {} = {}".format(description, num1 + num2)

def sub(num1, num2):
    description = "{} - {} ".format(num1, num2)
    return "The result of {} = {}".format(description, num1 - num2)

def mult(num1, num2):
    description = "{} * {} ".format(num1, num2)
    return "The result of {} = {}".format(description, num1 * num2)

def div(num1, num2):
    description = "{} / {} ".format(num1, num2)
    return "The result of {} = {}".format(description, num1 / num2)

def calc():
    allowed_calculations = {"+": add, "-": sub, "*": mult, "/": div}
    try:
            result = allowed_calculations[operator](first_num, second_num)
            print(result)

    except KeyError:
        print("The parameter doesn't exists.")
    except ZeroDivisionError:
        print("Can't divide by 0.")

calc()

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
