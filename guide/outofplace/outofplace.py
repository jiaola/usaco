import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    line = []
    n = int(input())
    for i in range(n):
        line.append(int(input()))

    b = -1

    left = True
    if line[0] > line[1]:
        b = 0
    elif line[-1] < line[-2]:
        b = n-1
        left = False
    else:
        for i in range(1, n-1):
            if line[i-1] > line[i]:
                if line[i-1] > line[i+1]:
                    b = i-1
                else:
                    b = i
                    left = False

    nums = []
    if left:
        for i in range(b, n):
            if line[i] < line[b]:
                nums.append(line[i])
    else:
        for i in range(b):
            if line[i] <= line[b]:
                continue
            nums.append(line[i])
    print(len(set(nums)))
    # an easier method
    # line2 = sorted(line)
    # total = len([i for i in range(n) if line[i] != line2[i]])
    # print(total - 1)


if __name__ == "__main__":
    main('outofplace')
