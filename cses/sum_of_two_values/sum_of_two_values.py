import sys


def main(pname):
    # sys.stdin = open(pname + 'in', 'r')
    # sys.stdout = open(pname + '.out', 'w')
    n, s = map(int, input().split())
    l = [int(i) for i in input().split()]
    l = list(zip(l, list(range(1, n+1))))
    l.sort()
    i = 0
    j = n-1
    while i < j:
        if l[i][0] + l[j][0] == s:
            print(l[i][1], l[j][1])
            break
        elif l[i][0] + l[j][0] < s:
            i += 1
        else:
            j -= 1
    if i == j:
        print('IMPOSSIBLE')


if __name__ == "__main__":
    main('1164')
