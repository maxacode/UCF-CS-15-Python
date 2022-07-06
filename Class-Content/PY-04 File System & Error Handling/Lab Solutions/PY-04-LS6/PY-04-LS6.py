"""Lab Objective: Create a directory and a file in that directory using the OS module."""

import os
import datetime

while True:
    print("Current directory: " + os.getcwd())
    new_dir_name = input("Choose a name for a new directory: ")
    os.mkdir(new_dir_name)
    os.chdir(new_dir_name)
    print("Current directory: " + os.getcwd())
    if new_dir_name:
        try:
            file_name = input("Choose a text file name ")
            with open("{}.txt".format(file_name), "w+") as new_file:
                new_file.write("Good job! New file was created on: " + str(datetime.datetime.now()))
                print("The following files are in the directory: " + str(os.listdir()))
                break
        except:
            print("Error")


input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
