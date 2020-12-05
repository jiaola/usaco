import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    lst = list(input())
    pos = {}
    for i in range(len(lst)):
        c = lst[i]
        if c not in pos:
            pos[c] = []
        pos[c].append(i)
    t = 0
    for i in range(26):
        c1 = chr(ord('A') + i)
        for j in range(i+1, 26):
            c2 = chr(ord('A') + j)
            if (pos[c1][0] < pos[c2][0] < pos[c1][1] < pos[c2][1]) or (pos[c2][0] < pos[c1][0] < pos[c2][1] < pos[c1][1]):
                t += 1
    print(t)


if __name__ == "__main__":
    main('circlecross')
