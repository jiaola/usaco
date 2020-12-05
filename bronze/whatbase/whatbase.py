import sys


def base_to_10(b, n):
    return int(n[0]) * b * b + int(n[1]) * b + int(n[2])


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    k = int(input())
    for i in range(k):
        n1, n2 = input().split()
        x = 10
        y = 10

        c1 = base_to_10(x, n1)
        c2 = base_to_10(y, n2)
        while c1 != c2:
            if c1 > c2:
                y += 1
            else:
                x += 1
            c1 = base_to_10(x, n1)
            c2 = base_to_10(y, n2)
        print(x, y)


if __name__ == "__main__":
    main('whatbase')
