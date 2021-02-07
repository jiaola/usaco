import sys
import math


def main(pname):
    # sys.stdin = open(pname + '.in', 'r')
    a = int(input())
    b = int(input())
    c = int(input())
    t1 = a * 3 + b * 2 + c

    a = int(input())
    b = int(input())
    c = int(input())
    t2 = a * 3 + b * 2 + c

    if t1 > t2:
        print("A")
    elif t1 == t2:
        print("T")
    else:
        print("B")


if __name__ == "__main__":
    main('prob1')
