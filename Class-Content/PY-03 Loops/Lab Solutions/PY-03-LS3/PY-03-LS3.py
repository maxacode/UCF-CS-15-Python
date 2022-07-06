"""Lab Purpose:Understand different ways to work with while loops to control the program flow."""

counter = 0

while counter < 10:
    counter += 1
    if counter == 6:
        print("Found!")
        break
    else:
        print("Check {}".format(counter))

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
