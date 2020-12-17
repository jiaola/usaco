import sys
from math import ceil, floor


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    b = [int(i) for i in list(input())]

    dist = []
    d = 0
    for i in range(n):
        if b[i] == 0:
            d += 1
        else:
            dist.append(d)
            d = 0
    dn = d
    if d == n:
        print(n-1)
        sys.exit()

    d0 = dist.pop(0)
    dist.sort()

    if len(dist) == 0:
        if d0 == 0:
            print(ceil((dn-1)/2))
        elif dn == 0:
            print(ceil((d0-1)/2))
        else:
            print(min(d0, dn))
        sys.exit()

    answer = 0
    if dist[-1] > 3:
        answer = max(answer, min(ceil((dist[-1]-1)/3), dist[0]+1))
        answer = max(answer, min(ceil(dist[-1]/2), dist[0]+1, max(d0, dn)))

    if len(dist) >= 2:
        answer = max(answer, min(ceil(dist[-2]/2), dist[0]+1))

    answer = max(answer, min(ceil((d0-1)/2), dist[0]+1))
    answer = max(answer, min(ceil((dn-1)/2), dist[0]+1))
    answer = max(answer, min(d0, dn))

    print(answer)


if __name__ == "__main__":
    main('socdist1')
