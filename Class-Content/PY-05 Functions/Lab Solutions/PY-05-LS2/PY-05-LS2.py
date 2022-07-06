"""Lab Objective: Create multiple functions that return different list types and check their types."""

def returned_list(first, second):
    return [first, second]


def returned_dict(first, second):
    return {first: second}


def returned_tup(first, second):
    return first, second


def returned_none(first, second):
    res = first + second


def main():
    first_val = input("Please enter a value: ")
    second_val = input("Please enter another value: ")
    list_res = returned_list(first_val, second_val)
    dict_res = returned_dict(first_val, second_val)
    tup_res = returned_tup(first_val, second_val)
    none_res = returned_none(first_val, second_val)
    print("{} and its type is: {}".format(list_res, type(list_res)))
    print("{} and its type is: {}".format(dict_res, type(dict_res)))
    print("{} and its type is: {}".format(tup_res, type(tup_res)))
    print("{} and its type is: {}".format(none_res, type(none_res)))


main()

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
