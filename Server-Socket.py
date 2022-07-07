"""Lab Objective: Implement the required commands to create a listening server."""
from audioop import add
import socket

print("Starting Server!")
my_sock = socket.socket()
my_sock.bind(("0.0.0.0", 4444))

print("Waiting for connections!.....")
my_sock.listen(1)
connection, address = my_sock.accept()
print(f"Connection Variable: {connection} \n Address Variable: {address}")

my_sock.close()


input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
