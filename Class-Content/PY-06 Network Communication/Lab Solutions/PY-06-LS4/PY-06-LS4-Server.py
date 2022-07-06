"""Lab Objective: Create a login interface using sockets."""
import socket

s = socket.socket()
s.bind(("0.0.0.0", 4321))
s.listen(1)
conn, addr = s.accept()
conn.send("Welcome to the server!\nPlease insert your Username:".encode())
username = conn.recv(2048).decode()
conn.send("Please insert the Password:".encode())
password = conn.recv(2048).decode()
if username == "John" and password == "12345":
    conn.send(f"Welcome {username}".encode())
else:
    conn.send("Wrong username or password".encode())

s.close()

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
