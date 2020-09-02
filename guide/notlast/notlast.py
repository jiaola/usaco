import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    cows = {}
    n = int(input())
    for i in range(n):
        c, k = input().split()
        cows[c] = cows.get(c, 0) + int(k)
    v = set(cows.values())
    if len(cows) < 7:
        v.add(0)
    s = sorted(v)

    if len(s) == 1:
        print('Tie')
    else:
        name = [k for k, v in cows.items() if v == s[1]]
        if len(name) > 1:
            print('Tie')
        else:
            print(name[0])


if __name__ == "__main__":
    main('notlast')
