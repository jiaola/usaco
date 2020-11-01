import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    a = input()
    b = input()
    same = True
    t = 0
    for i in range(n):
        if a[i] == b[i]:
            same = True
        else:
            if same:
                t += 1
                same = False

    print(t)


if __name__ == "__main__":
    main('breedflip')
