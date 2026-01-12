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