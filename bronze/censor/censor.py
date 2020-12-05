import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    s = input()
    t = input()
    l = len(t)

    o = ''
    for i in s:
        o += i
        if o[-l:] == t:
            o = o[:-l]
    print(o)


if __name__ == "__main__":
    main('censor')
