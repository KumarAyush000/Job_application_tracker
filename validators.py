"""
Docstring for validators

will contain all the reusable parts of the code in skills_manager.py
"""

def empty_input_checker(name):
    if not name:
        return True
    else:
        return False
    
def empty_list_checker(lst):
    if not lst:
        return True
    else:
        return False
    
def to_int(input_string):
    # on success -> int
    if input_string.isdigit():
        input_string = int(input_string)
        return input_string
    # on failure -> none
    else:
        return None