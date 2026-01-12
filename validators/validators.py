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
    
def get_valid_index(input_value, items):
    if not input_value:
        return None
    
    if not input_value.isdigit():
        return None
    
    index = int(input_value)
    
    if index < 1 or index > len(items):
        return None
    
    # if index is valid reducing it by 1 to make it indexable
    return index -1
        
        
            