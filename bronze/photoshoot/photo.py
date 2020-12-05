import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    b = [int(i) for i in input().split()]
    for a_i in range(1, b[0]):
        a = list()
        a.append(a_i)
        for j in b:
            a_i = j - a_i
            if a_i <= 0:
                break
            a.append(a_i)
        if len(set(a)) == n:
            print(" ".join([str(i) for i in a]))


if __name__ == "__main__":
    main('photo')
