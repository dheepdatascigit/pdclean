# Python Data tools

import re
import math
import numpy as np
import pandas as pd
import scipy as sp


import re, math

def extract_num(in_str, select_logic='all'):
    """ extract numbers from the string output one number based on select logic
    
        selelct logic = 
            - 'all' -- all items in a list (default)
            - 'first' -- first of the item
            - 'mean' -- mean of two numbers
            - 'sum' -- sum of all items

    """
    
    #str_list = re.findall(r'[\+\-]?[0-9]+', str(in_str))
    num_list = [] #initialize list
    
    for i in str(in_str).split():
        try:
            temp_num = float(i)
            num_list.append(temp_num)
        except ValueError:
            pass
    
    if select_logic == 'sum':
        num_out = sum(num_list)
    elif select_logic == 'mean':
        num_out = np.mean(num_list)
    elif select_logic == 'first':
        num_out = num_list[0]
    else:
        num_out = num_list
    
    return num_out
    


if __name__ == "__main__":
    pass
