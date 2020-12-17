import sys


def main(file):
    sys.stdin = open(file + '.in', 'r')
    sys.stdout = open(file + '.out', 'w')
    n = int(input())
    d = dict()
    for i in range(n):
        a = input().split()
        d[int(a[0])] = int(a[1])
    d = list(sorted(d.items()))
    mindist = 10 ** 7
    for i in d:
        if i[1] == 0:
            for j in d:
                if i != j:
                    if j[1] == 1:
                        mindist = min(abs(j[0] - i[0]), mindist)
    r = mindist - 1
    for i in d:
        if i[1] == 1:
            prev = i[0]
            lst = [[prev]]
            for j in d:
                if j[0] == prev:
                    continue
                if j[1] == 0:
                    continue
                if j[0] - prev <= r:
                    lst[-1].append(j[0])
                else:
                    lst.append([j[0]])
                prev = j[0]
            print(len(lst))
            break


if __name__ == '__main__':
    main('socdist2')