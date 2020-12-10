import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n, b = [int(i) for i in input().split()]
    x = []
    y = []
    for i in range(n):
        xi, yi = [int(j) for j in input().split()]
        x.append(xi)
        y.append(yi)
    min_max = n
    for a in x:
        for b in y:
            zones = [0] * 4
            for j in range(n):
                if x[j] < a+1 and y[j] < b+1:
                    zones[0] += 1
                elif x[j] < a+1 and y[j] > b+1:
                    zones[1] += 1
                elif x[j] > a+1 and y[j] < b+1:
                    zones[2] += 1
                else:
                    zones[3] += 1
            min_max = min(min_max, max(zones))
    print(min_max)


if __name__ == "__main__":
    main('balancing')
