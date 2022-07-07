"""Lab Objective: Create a login interface using sockets."""

import socket

s = socket.socket()
s.connect(("127.0.0.1", 4321))
print(s.recv(2048).decode())
s.send(input("").encode())
print(s.recv(2048).decode())
s.send(input("").encode())
print(s.recv(2048).decode())
s.close()

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
