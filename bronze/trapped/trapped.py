import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    N = int(input())
    bales = []
    for i in range(N):
        s, x = [int(i) for i in input().split()]
        bales.append((x, s))
    bales.sort()
    total = 0
    for i in range(N-1):
        delta = bales[i+1][0] - bales[i][0]
        left = i
        right = i+1
        while left >= 0 and right < N:
            free = False
            dist = bales[right][0] - bales[left][0]
            if dist > bales[left][1]:
                left -= 1
                free = True
            if dist > bales[right][1]:
                right += 1
                free = True
            if not free:
                break
        if left >= 0 and right < N:
            total += delta
    print(total)


if __name__ == "__main__":
    main('trapped')
