#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    arr = []
    k = 0
    for i in range(len(topic)):
        k += 1
        for j in range(k, len(topic)):
            counter = 0
            for l in range(len(topic[0])):
                if topic[i][l] == '1' or topic[j][l] == '1':
                    counter += 1
            arr.append(counter)
    return [max(arr), arr.count(max(arr))]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
