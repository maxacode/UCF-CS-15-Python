"""Lab Objective: Print text lines from a file."""

path = input("Enter a directory path for the text file: ")
filename = input("Enter full filename: ")

file = open(path+"\\"+filename, "r")
for line in file:
    print(line)

file.close()

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
