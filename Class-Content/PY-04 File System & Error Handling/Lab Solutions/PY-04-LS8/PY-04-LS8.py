"""Lab Objective: Practice working with the OS module."""

import os

try:
    os.mkdir(r"C:\Users\johnd\Downloads\Cars")
except:
    print("This directory already exists")
with open(r"C:\Users\johnd\Downloads\Cars\Mustang.txt", "a+") as file:
    pass

path = input("Enter directory path: ")
file_name = input("Enter file name: ")
new_name = input("Enter a new name: ")

os.system(r"copy {}\{} {}\{}".format(path, file_name, path, new_name))

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
