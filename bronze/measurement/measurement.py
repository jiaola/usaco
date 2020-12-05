import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    r = []
    for i in range(n):
        l = input().split()
        l[0] = int(l[0])
        r.append(l)
    r.sort(key=lambda x: x[0])

    milk = {'Bessie': 7, 'Elsie': 7, 'Mildred': 7}
    cows = ['Bessie', 'Elsie', 'Mildred']
    highest = ['Bessie', 'Elsie', 'Mildred']
    c = 0
    # 7 Bessie -3
    for i in r:
        cow = i[1]
        change = i[2]
        milk[cow] += int(change)
        m = max(milk.values())
        new_highest = [i for i in cows if milk[i] == m]
        new_highest.sort()
        if highest != new_highest:
            c += 1
        highest = new_highest
    print(c)


if __name__ == "__main__":
    main('measurement')
