#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    s.replace(" ", "")
    length = len(s)
    obtained_string = ""
    col = math.ceil(math.sqrt(length))
    row = math.floor(length/ col)
    for i in range(col):
        j = i
        while j < length:
            obtained_string += s[j]
            j += col
        if i != col -1:
            obtained_string += " "
    return obtained_string




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
