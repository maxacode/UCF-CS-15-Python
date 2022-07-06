"""Lab Objective: Practice using a dictionary that stores predefined data extracted randomly by users."""

print ("This program will display the port number of a given protocol\n") # explains the purpose of the script


ProtocolsDict = {'FTP': '21', 'DNS': '53', 'LDAP': '389', 'MySQL': '3306'}
question = input("For which protocol would you like to know the port number? ")
if question in ProtocolsDict.keys():
    answer = ProtocolsDict[question]
    print("The port number for protocol " + question + " is " + answer + "!")
   
else:
    print("The protocol can't be found")
    
input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
