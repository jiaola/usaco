import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    s = input()
    t = input()
    l = len(t)

    o = ''
    i = s.find(t)
    start = 0
    while i >= 0:
        i += start
        s = s[:i] + s[i + l:]
        start = max(0, i-l+1)
        i = s[start:].find(t)
    print(s)


if __name__ == "__main__":
    main('censor')
