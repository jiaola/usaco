import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n, m, d, s = [int(i) for i in input().split()]
    person = []
    sp = [-1] * n
    for i in range(n):
        milk = []
        for j in range(m):
            milk.append([])
        person.append(milk)

    for i in range(d):
        p, ma, t = [int(j) for j in input().split()]
        person[p-1][ma-1].append(t)
    for i in range(s):
        p, t = [int(j) for j in input().split()]
        sp[p-1] = t

    max_doses = 0

    for i in range(m):
        possible = True
        count = 0
        for j in range(n):
            st = sp[j]
            drink_times = person[j][i]
            if len(drink_times) == 0:
                if st != -1:  # didn't drink but got sick
                    possible = False
                    break
                else:
                    continue
            count += 1
            if min(drink_times) >= st > -1:
                possible = False
                break
        if possible:
            max_doses = max(max_doses, count)
    print(max_doses)


if __name__ == "__main__":
    main('badmilk')
