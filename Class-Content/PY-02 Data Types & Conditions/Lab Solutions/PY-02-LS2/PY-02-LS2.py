name = input("What is your name? ")
age = input("What is your age? ")
age = int(age)
print("Hello {}, your age is {}".format(name, age))
if age >= 21:
    print("You can buy an alcoholic beverage")
else:
    print("You cannot buy an alcoholic beverage")

input("\nPress 'Enter' to exit this program.")

