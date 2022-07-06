"""Lab Objective: Practice working with files and error handling."""

try:
    with open("text.txt", "r") as text:
        text.write("Test")

except Exception:
    print("Unsupported Operation, cannot write in read mode.")