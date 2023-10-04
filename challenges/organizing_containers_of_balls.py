#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    size_of_container = []
    arr = []
    i = 0
    while i < len(container[0]):
        total = 0
        for box in container:
            total += box[i]
            if i == 0:
                size_of_container.append(sum(box))
        i += 1
        arr.append(total)
    arr.sort()
    size_of_container.sort()
    if arr == size_of_container:
        return "Possible"
    else:
        return "Impossible"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
