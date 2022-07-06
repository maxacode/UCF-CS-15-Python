""""Lab Objective: Understand how to work with user-defined dictionaries to control the program flow."""

servicePorts = {}

while True:
    service = input("Please enter a service's name or type '0' to stop: ")
    if service == "0":
        break

    port = input("Please enter a port number or type '0' to stop: ")
    if port == "0":
        break

    servicePorts[service] = port

print(servicePorts)


input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
