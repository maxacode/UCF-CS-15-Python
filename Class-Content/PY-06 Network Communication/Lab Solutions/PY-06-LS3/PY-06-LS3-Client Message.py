"""Lab Objective: Create a server socket and a client socket and enable them to communicate with each other."""
import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 45000))
print(sock.recv(2048).decode())
sock.send("Thanks!".encode())
sock.close()

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
