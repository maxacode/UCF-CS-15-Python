"""Lab Objective: Practice handling errors that may occur in the code."""

product = 1
for i in range(4):
    try:
        num = int(input("Enter a number: "))
        product *= num
    except:
        print("The input is not a valid number")
print("The product of the 4 numbers is: " + str(product))

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
