import sys, itertools


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    t = 0
    for i in l:
        m = list(filter(lambda a: a != i, l))
        dups = [sum(1 for _ in group) for _, group in itertools.groupby(m)]
        t = max(t, max(dups))
    print(t)


if __name__ == "__main__":
    main('cowrow')
