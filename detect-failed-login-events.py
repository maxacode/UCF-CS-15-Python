"""
Detect windows login failed events. 

Create an alert when 3 failed logins in a 5min span per user/machine. 

Create an alert after 50 failed logins if a Succesful one happens within 10min.

"""

logs= [
    {'Date': '07-06-2022', 'Time': '6:54', 'Username': 'Bob' ,'Event': 'Succesfull Logon', "IP Address": "13.1.5.15"},
    {'Date': '07-06-2022', 'Time': '6:55', 'Username': 'Administrator' ,'Event': 'Failed Logon', "IP Address": "13.1.5.15"},
    {'Date': '07-06-2022', 'Time': '6:56', 'Username': 'Administrator' ,'Event': 'Failed Logon', "IP Address": "13.1.5.15"},
    {'Date': '07-06-2022', 'Time': '6:56', 'Username': 'Administrator' ,'Event': 'Succesfull Logon', "IP Address": "13.1.5.15"},
    {'Date': '07-06-2022', 'Time': '6:57', 'Username': 'Administrator' ,'Event': 'Failed Logon', "IP Address": "13.1.5.15"}
]

failedTimes = 0
timeOfFailLogin = 0

for singleLog in logs:
    #print(singleLog)
    if singleLog['Event'] == "Failed Logon":
        failedTimes += 1
        if failedTimes >= 3:
            print("ALERT! To many Failed Logins! BRUTE FORCE ATTEMPT")

        if singleLog['Time'] - timeOfFailLogin < 5:
            continue

        else:
            failedTimes = 0
            continue
        



