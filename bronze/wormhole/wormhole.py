import sys


def check_cycle(pairs, right):
    for i in range(len(right)):
        current = i
        j = 0
        cycle = True
        while j < len(pairs):
            current = right[current]
            if current == -1:
                cycle = False
                break
            current = pairs[current]
            j += 1
        if cycle:
            return 1
    return 0


def pairing(right, pairs):
    try:
        first = pairs.index(-1)
    except ValueError:
        return check_cycle(pairs, right)
    total = 0
    for j in range(first+1, len(right)):
        if pairs[j] == -1:
            pairs[first] = j
            pairs[j] = first
            total += pairing(right, pairs)
            pairs[first] = -1
            pairs[j] = -1
    return total


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    points = []
    for i in range(n):
        points.append([int(j) for j in input().split()])
    right = [-1] * n
    for i in range(n):
        min_dist = 10 ** 10 + 1
        for j in range(n):
            if i == j:
                continue
            if points[j][1] == points[i][1] and points[j][0] > points[i][0]:
                if points[j][0] - points[i][0] < min_dist:
                    right[i] = j
                    min_dist = points[j][0] - points[i][0]

    pairs = [-1] * n
    print(pairing(right, pairs))


if __name__ == "__main__":
    main('wormhole')
