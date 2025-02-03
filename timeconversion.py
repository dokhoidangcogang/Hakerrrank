#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    period = s[-2:]
    time = s[:-2]
    
    hh,mm,ss = time.split(':')
    
    if(period == 'PM'):
        if hh != '12':
            hh = str(int(hh) + 12)
    else:
        if hh == '12':
            hh = '00'
    return f"{hh}:{mm}:{ss}"                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
