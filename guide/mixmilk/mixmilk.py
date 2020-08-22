# Original code by Jerry G, and modified by Dazhi Jiao

import sys


def mix(mf, bt, mt):
    p = min(mf, bt - mt)
    return mf - p, mt + p


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    b1, m1 = map(int, input().split())
    b2, m2 = map(int, input().split())
    b3, m3 = map(int, input().split())
    for i in range(33):
        m1, m2 = mix(m1, b2, m2)
        m2, m3 = mix(m2, b3, m3)
        m3, m1 = mix(m3, b1, m1)
    m1, m2 = mix(m1, b2, m2)

    print(m1)
    print(m2)
    print(m3)


if __name__ == "__main__":
    main('mixmilk')
