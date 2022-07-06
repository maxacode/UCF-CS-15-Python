"""Lab Objective: Implement a recursion to print values from a nested list."""
lst = [
    1, #0
    2, #1
    "a", #2
    [4, 5, "b", 6],  #3
    [7, 
    [8, "d", 9]
    ]
    ]

 

def print_numbers(item_list):
	for item in item_list:
		if type(item) == int or type(item) == str:
			print(item)
		elif type(item) == list:
			print_numbers(item)

print_numbers(lst)
