#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    s = (("0" + str((int(s[:2])+12) % 12))[-2:] if s[-2:] == "AM" else str(12 + int(s[:2])%12)) + s[2:-2]
    return s


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
