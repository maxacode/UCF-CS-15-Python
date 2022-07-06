"""Lab Objective: Create a client socket."""
import socket
import time

my_socket = socket.socket()
my_socket.connect(("10.0.0.5", 4444))
time.sleep(5)
my_socket.close()

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
