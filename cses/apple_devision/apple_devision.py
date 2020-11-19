import sys


# def solve(i, l, s1, s2):
#     if i == len(l):
#         return abs(s2 - s1)
#     return min(solve(i+1, l, s1+l[i], s2), solve(i+1, l, s1, s2+l[i]))


def solve(l, sa, sb):
    if len(l) == 0:
        return abs(sa - sb)
    else:
        least = 10 ** 12
        for i in range(len(l)):
            new_l = l[:i]+l[i+1:]
            least = min(least, solve(new_l, sa+l[i], sb), solve(new_l, sa, sb+l[i]))
    return least


def main(pname):
    # sys.stdin = open(pname + '.in', 'r')
    # sys.stdout = open(pname + '.out', 'w')
    n = int(input())
    l = [int(i) for i in input().split()]
    print(solve(l, 0, 0))


if __name__ == "__main__":
    main('apple_devision')
