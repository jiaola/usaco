import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    N = int(input())
    f = []
    for i in range(N):
        f.append(list(input()))




if __name__ == "__main__":
    main('palpath')
