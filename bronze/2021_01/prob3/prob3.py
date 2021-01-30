import sys


def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    a.reverse()
    ans = 1
    for i in range(0, len(a)-1):
        ai = a[i]
        c = 0
        for bi in b:
            if bi >= ai:
                c += 1
        ans *= (c - i)
    print(ans)


if __name__ == '__main__':
    main()