"""Lab Objective: Practice using advanced conditions and handling out-of-range values."""

print ("This program will calcuate and display the letter grade of a numerical value\n") # explains purpose of the script
grade = int(input("Enter a grade: "))

if grade >= 90:
    print("Letter grade: A")
elif grade >= 80:
    print("Letter grade: B")
elif grade >= 70:
    print("Letter grade: C")
elif grade >= 65:
    print("Letter grade: D")
elif grade >= 0:
    print("Letter grade: F")

# Will be printed if the value is a negative number or a word.
else:
    print("ERROR: Grades cannot be negative numbers or words.")
input("\nPress 'Enter' to exit the program") # prevents program from closing upon execution
