
# import typing

# def print_something(something="привет", times = 5):
#     # print(something)
#     # print(times)
#     """
#     Var {something} == String
#     Var {times} == int


#     """
#     list1 = []
#     for x in range(times):
#         list1.append(something)
#     return {something: times}

#     #return print({"list1": list1, "Times": times})


# print(print_something())

from random import randrangedef 
main():    
dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}    
dice_roll_res(dice)def dice_rolling():    
rolls = int(input("Times to roll the dice: ")) 
print("Rolling the dice")

return rollsdef dice_roll_res(dice): for i in range(dice_rolling()):        roll_res = randrange(1, 7)        dice[roll_res] += 1 print(dice)main()
