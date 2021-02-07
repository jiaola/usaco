import sys


def main(name):
    sys.stdin = open(name + '.in', 'r')
    sys.stdout = open(name + '.out', 'w')

    n = int(input())
    x_values = []
    y_values = []
    area = 2500000000
    for i in range(n):
        x, y = map(int, input().split())
        x_values.append(x)
        y_values.append(y)
    x_values.sort()
    y_values.sort()

    x_values_copy = x_values[1:]
    y_values_copy = y_values[1:]
    x_length = x_values_copy[-1] - x_values_copy[0]
    y_length = y_values_copy[-1] - y_values_copy[0]
    area = min(x_length * y_length, area)

    x_values_copy2 = x_values[:-1]
    y_values_copy2 = y_values[:-1]
    x_length2 = x_values_copy2[-1] - x_values_copy2[0]
    y_length2 = y_values_copy2[-1] - y_values_copy2[0]
    area = min(x_length2 * y_length2, area)
    print(area)


if __name__ == "__main__":
    main('reduce')
