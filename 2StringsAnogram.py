# if 2 given strings are Anograms = God Dog = True.. Not couting Spaces and Capitilziation 
# ex 2: clint eastwood  = old west action = True

# string1 = "God Is Good"
# string2 = "Dogigoos d"

# #test 2
# string1 = "clint eastwood"
# string2 = "old west action"


# def anogramTest(string1, string2):
#     string1 = string1.lower().replace(' ', '')
#     string2 = string2.lower().replace(' ', '')
#     if len(string1) >= len(string2):
#         longString = string1
#     else:
#         longString = string2
#     for x in longString:
#         if string1.count(x) == string2.count(x):
#             #print(string1.count(x))
#             if x == longString[-1]:
#                 return print("True Anogram")

#         else:

#             return print("False")




#test 2
string1 = "clint eastwood f"
string2 = "old west action jjkk"


#Same test just returns what other Chars and count is needed to make true. 
def anogramTestToMakeTrue(string1, string2):
    string1 = string1.lower().replace(' ', '')
    string2 = string2.lower().replace(' ', '')
    chars = {}
    
    if len(string1) >= len(string2):
        longString = string1
    else:
        longString = string2

    for x in longString:
        if string1.count(x) == string2.count(x):
            #print(string1.count(x))
            if x == longString[-1]:
                return print("True Anogram")

        else:
            chars[x] = (string1.count(x) + string2.count(x))
            if x == longString[-1]:
                return print(chars)

anogramTestToMakeTrue(string1, string2)