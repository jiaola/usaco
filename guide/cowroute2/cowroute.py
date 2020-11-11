import sys


def check_pair(r1, r2, a, b):
    try:
        ind_a = r1.index(a)
    except ValueError:
        ind_a = -1
    try:
        ind_b = r2.index(b)
    except ValueError:
        ind_b = -1
    if a > -1 and b > -1:
        if not set(r1[ind_a+1:]).isdisjoint(r2[:ind_b]):
            return True
    return False


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    a, b, n = [int(i) for i in input().split()]
    routes_a = []
    costs_a = []
    routes_b = []
    costs_b = []
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
        if ind_a > -1:
            routes_a.append(r)
            costs_a.append(cost)
        if ind_b > -1:
            routes_b.append(r)
            costs_b.append(cost)
    for i in range(len(routes_a)):
        for j in range(len(routes_b)):
            if check_pair(routes_a[i], routes_b[j], a, b):
                min_cost = min(min_cost, costs_a[i] + costs_b[j])
    if min_cost < 10000:
        print(min_cost)
    else:
        print(-1)


if __name__ == "__main__":
    main('cowroute')
