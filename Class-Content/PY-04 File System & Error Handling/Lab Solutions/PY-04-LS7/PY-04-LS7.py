"""Lab Objective: Encode and decode a Base64 secret using Python and print the original message to the console."""
import base64

secret = input("Please enter a secret: ")
encoded = base64.b64encode(secret.encode("utf-8"))
decoded = base64.b64decode(encoded)
print("The encoded string is ", encoded)
print("The decoded string is ", decoded)

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
