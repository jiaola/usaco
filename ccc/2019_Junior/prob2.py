import sys
import math


def main(pname):
    n = int(input())
    for i in range(n):
        a, b = input().split()
        a = int(a)
        print(b * a)


if __name__ == "__main__":
    main('prob1')
