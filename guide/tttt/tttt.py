import sys


def check_cow(b, cow):
    # rows
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] == cow:
            return True
        if b[0][i] == b[1][i] == b[2][i] == cow:
            return True
    if b[0][0] == b[1][1] == b[2][2] == cow:
        return True
    if b[0][2] == b[1][1] == b[2][0] == cow:
        return True
    return False


def check_pair(b, pair):
    for i in range(3):
        s = set(b[i])
        if len(s) == 2 and pair[0] in s and pair[1] in s:
            return True
        s = set([b[0][i], b[1][i], b[2][i]])
        if len(s) == 2 and pair[0] in s and pair[1] in s:
            return True
    s = set([b[0][0], b[1][1], b[2][2]])
    if len(s) == 2 and pair[0] in s and pair[1] in s:
        return True
    s = set([b[0][2], b[1][1], b[2][0]])
    if len(s) == 2 and pair[0] in s and pair[1] in s:
        return True
    return False


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    cows = set()
    b = []
    for i in range(3):
        row = list(input())
        cows.update(row)
        b.append(row)
    cows = list(cows)
    c_cows = 0
    for cow in cows:
        if check_cow(b, cow):
            c_cows += 1

    c_pairs = 0
    for i in range(len(cows)):
        for j in range(0, i):
            if check_pair(b, (cows[i], cows[j])):
                c_pairs += 1
    print(c_cows)
    print(c_pairs)


if __name__ == "__main__":
    main('tttt')
