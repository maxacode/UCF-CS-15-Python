"""Lab Objective: Practice working with different types of data structures."""

print ("This program will c\n") # explains the purpose of the script

structure = [{'Arizona': 'Phoenix', 'California': 'Sacramento', 'Hawaii': 'Honolulu'},
             5000,6000,7000,['hat', 't-shirt', 'jeans']]

print(structure[1])
print(structure[0])
print(structure[4])
print(structure[0]['Arizona'])
print(structure[4][2])
del(structure[3])
print(structure)
structure.append("new value")
print(structure)

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
