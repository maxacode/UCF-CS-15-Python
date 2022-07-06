"""Lab Objective: Implement recursion with various functions of the OS library."""
import os
import sys

# A variable used for formatting.
line = "<----------------------------------------------------------->"
system = sys.platform
print("You are using {}".format(system))
root_folder = input("Enter folder: ")

# Prints files and their size found recursively in a specified path
# Includes formatting for easier understanding of the program.
def mapper(path):
    try:
        # iteration over the files and directories of the path.
        for item in os.listdir(path):
            full_path = r"{}\{}".format(path, item)
            # Check the type of the item, prints files or enter into directories recursively.
            if os.path.isfile(full_path):
                size = os.stat(full_path).st_size
                print("Found {} -> weighs {} bytes.".format(full_path, size))
            elif os.path.isdir(full_path):
                print("{}\nEntering folder {}\n{}".format(line, item, line))
                mapper(full_path)
            else:
                print("Unknown.")

    except Exception as error:
        print(error)


mapper(root_folder)

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
