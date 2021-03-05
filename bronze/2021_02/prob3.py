import sys


def main(pname):
    # sys.stdin = open(pname + '.in', 'r')
    ct = 0
    cct = 0
    cw = 'NESWN'
    ccw = 'NWSEN'
    N = int(input())
    # reduce to only turns
    for i in range(N):
        line = input()
        for j in range(1, len(line)):
            if line[j] != line[j-1]:
                if line[j-1:j+1] in cw:
                    ct += 1
                else:
                    cct += 1
        if ct > cct:
            print('CW')
        else:
            print('CCW')
        ct = 0
        cct = 0


if __name__ == "__main__":
    main('prob3')
