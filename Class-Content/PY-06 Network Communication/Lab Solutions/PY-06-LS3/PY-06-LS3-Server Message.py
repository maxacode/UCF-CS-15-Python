"""Lab Objective: Create a server socket and a client socket and enable them to communicate with each other.
"""
import socket

sock = socket.socket()
sock.bind(("0.0.0.0", 45000))
sock.listen(1)
conn, addr = sock.accept()
conn.send("Welcome to the server!".encode())
print(conn.recv(2048).decode())
sock.close()

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
