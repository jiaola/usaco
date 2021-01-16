import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    N = int(input())
    x = []
    y = []
    max_x = 0
    max_x_2 = 0
    min_x = 40000
    min_x_2 = 40000
    max_y = 0
    max_y_2 = 0
    min_y = 40000
    min_y_2 = 40000
    for i in range(N):
        a, b = [int(i) for i in input().split()]
        x.append(a)
        y.append(b)
        if max_x < a:
            max_x_2 = max_x
            max_x = a
        elif max_x_2 < a:
            max_x_2 = a
        if min_x > a:
            min_x_2 = min_x
            min_x = a
        elif min_x_2 > a:
            min_x_2 = a
        if max_y < b:
            max_y_2 = max_y
            max_y = b
        elif max_y_2 < b:
            max_y_2 = b
        if min_y > b:
            min_y_2 = min_y
            min_y = b
        elif min_y_2 > b:
            min_y_2 = b

    area = (max_x - min_x) * (max_y - min_y)
    for i in range(N):
        min_x_copy = min_x
        if x[i] == min_x:
            min_x_copy = min_x_2
        max_x_copy = max_x
        if x[i] == max_x:
            max_x_copy = max_x_2
        min_y_copy = min_y
        if y[i] == min_y:
            min_y_copy = min_y_2
        max_y_copy = max_y
        if y[i] == max_y:
            max_y_copy = max_y_2
        area = min(area, (max_x_copy - min_x_copy) * (max_y_copy - min_y_copy))
    print(area)


if __name__ == "__main__":
    main('reduce')
