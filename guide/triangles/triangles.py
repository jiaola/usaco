import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    points = []
    for i in range(n):
        points.append([int(i) for i in input().split()])

    m = 0
    for i in range(n):
        max_x = 0
        max_y = 0
        for j in range(n):
            if i == j:
                continue
            if points[i][0] == points[j][0]:
                max_y = max(max_y, abs(points[j][1] - points[i][1]))
            elif points[i][1] == points[j][1]:
                max_x = max(max_x, abs(points[j][0] - points[i][0]))
        m = max(m, max_x * max_y)
    print(m)


if __name__ == "__main__":
    main('triangles')
