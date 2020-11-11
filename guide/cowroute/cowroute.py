import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    a, b, n = [int(i) for i in input().split()]
    min_cost = 10000
    for i in range(n):
        cost, nc = [int(j) for j in input().split()]
        r = [int(j) for j in input().split()]
        try:
            ind_a = r.index(a)
        except ValueError:
            ind_a = -1
        try:
            ind_b = r.index(b)
        except ValueError:
            ind_b = -1
        if -1 < ind_a < ind_b:
            min_cost = min(cost, min_cost)
    if min_cost < 10000:
        print(min_cost)
    else:
        print(-1)


if __name__ == "__main__":
    main('cowroute')
