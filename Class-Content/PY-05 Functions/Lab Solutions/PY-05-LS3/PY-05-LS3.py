"""Lab Objective: Create global variables and try to make changes to them within a function."""

global_var = 5
changed_global_var = 20

def local_change():
    _new_global_var = global_var
    print("inside function global_var's value: ", _new_global_var)
    global changed_global_var
    changed_global_var += 5
    print("inside function changed_global_var's value: ", changed_global_var)
    return _new_global_var

local_change()

print(__name__)
 