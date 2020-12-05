import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    s = input()

    for i in range(n):
        ss = set()
        for j in range(n-i):
            ss.add(s[j:j+i+1])
        if len(ss) == n-i:
            return i+1


if __name__ == "__main__":
    print(main('whereami'))
