import sys


def check(l, i):
    count = 1
    index = i
    r = 1
    low = l[index] - r
    while True:
        new_index = index
        for j in range(index - 1, -1, -1):
            if l[j] >= low:
                new_index = j
                count += 1
            else:
                break
        if new_index == index:
            break
        else:
            index = new_index
            r += 1
            low = l[index] - r

    index = i
    r = 1
    high = l[index] + r
    while True:
        new_index = index
        for j in range(index + 1, len(l)):
            if l[j] <= high:
                new_index = j
                count += 1
            else:
                break
        if new_index == index:
            break
        else:
            index = new_index
            r += 1
            high = l[index] + r
    return count


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    l.sort()
    max_count = 0
    for i in range(len(l)):
        max_count = max(max_count, check(l, i))
    print(max_count)


if __name__ == "__main__":
    main('angry')
