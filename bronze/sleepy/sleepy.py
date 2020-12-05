import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    lst = [int(i) for i in input().split()]

    # find the sorted in the end
    m = n - 1
    while True:
        if lst[m-1] > lst[m]:
            break
        m -= 1
    print(m)


if __name__ == "__main__":
    main('sleepy')
