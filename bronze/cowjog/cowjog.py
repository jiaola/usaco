import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    N = int(input())
    cows = []
    for i in range(N):
        cows.append([int(i) for i in input().split()])
    cows.sort()
    cows.reverse()
    t = 0
    slowest = cows[0][1]
    for i in range(N):
        cow = cows[i]
        if cow[1] > slowest:
            continue
        slowest = cow[1]
        t += 1
    print(t)


if __name__ == "__main__":
    main('cowjog')
