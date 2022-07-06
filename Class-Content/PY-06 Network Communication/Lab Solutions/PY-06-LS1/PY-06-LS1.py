"""Lab Objective: Implement the required commands to create a listening server."""
import socket

my_sock = socket.socket()
my_sock.bind(("0.0.0.0", 4444))
my_sock.listen(1)
connection, address = my_sock.accept()
my_sock.close()


input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
