#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    cz=cp=cn=0
    for x in range(len(arr)):
        if arr[x] > 0:
            cp+=1
        elif arr[x] < 0:
            cn+=1
        else:
            cz+=1
    print("%0.6f\n%0.6f\n%0.6f" % (cp/n, cn/n, cz/n) )
    return 0


        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
