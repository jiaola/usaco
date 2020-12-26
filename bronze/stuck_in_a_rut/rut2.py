import sys
from copy import deepcopy


def check_finished(current, stopped, direction):
    n = len(stopped)
    for i in range(n):
        if stopped[i]:
            continue
        for j in range(n):
            if direction[i] == direction[j]:
                continue
            if direction[i] == 'E':
                if current[i][0] < current[j][0]:
                    return False
            else:
                if current[i][1] < current[j][1]:
                    return False
    return True


def need_to_stop(position, start, current, index, direction):
    for i in range(len(current)):
        if i == index:
            continue
        if direction[i] == direction[index]:
            if direction[i] == 'E' and position[1] == start[i][1]:
                if position[0] == start[i][0]:
                    return True
            elif direction[i] == 'N' and position[0] == start[i][0]:
                if position[1] == start[i][1]:
                    return True
        else:
            if direction[index] == 'E':
                if position[0] == current[i][0] and start[i][1] <= position[1] <= current[i][1]:
                    return True
            else:
                if position[1] == current[i][1] and start[i][0] <= position[0] <= current[i][0]:
                    return True
    return False


def main(pname):
    sys.stdin = open(pname + '.in', 'r')

    n = int(input())
    direction = []
    start = []
    for i in range(n):
        d, x, y = input().split()
        x = int(x)
        y = int(y)
        direction.append(d)
        start.append([x, y])

    current = deepcopy(start)
    stopped = [False] * n

    time = 0
    while True:
        next_current = deepcopy(current)
        for i in range(n):
            if stopped[i]:
                continue
            if direction[i] == 'E':
                next_current[i][0] += 1
            else:
                next_current[i][1] += 1
        for i in range(n):
            if need_to_stop(next_current[i], start, current, i, direction):
                stopped[i] = True
        current = deepcopy(next_current)
        time += 1
        if check_finished(current, stopped, direction):
            break

    for i in range(n):
        if not stopped[i]:
            print('Infinity')
        else:
            if direction[i] == 'E':
                print(current[i][0] - start[i][0])
            else:
                print(current[i][1] - start[i][1])


if __name__ == '__main__':
    main('rut')