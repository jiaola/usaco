import sys


def main(name):
    sys.stdin = open(name + '.in', 'r')
    sys.stdout = open(name + '.out', 'w')

    n = int(input())
    lst = []
    total = 0
    shortest_distance = 0
    current_distance = 0
    for i in range(n):
        cows = int(input())
        lst.append(cows)
        total += cows
    for i in range(n):
        subtotal = total
        for j in lst:
            subtotal = subtotal - j
            current_distance += subtotal
        if shortest_distance >= current_distance or shortest_distance == 0:
            shortest_distance = current_distance
        current_distance = 0
        value = lst.pop(0)
        lst.append(value)
    print(shortest_distance)


if __name__ == "__main__":
    main('cbarn')