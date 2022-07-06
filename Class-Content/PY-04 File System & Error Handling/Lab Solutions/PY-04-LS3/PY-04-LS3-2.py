"""Lab Objective: Practice working with files and error handling."""
try:
    file = open("file.txt", "a")
    while True:
        message = input("Enter text! ('Exit' to exit): ")
        if message.lower() == "exit":
            break
        else:
            file.write(message + "\n")
    file.close()

except:
    print("An error occurred while trying to open the file.")

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
