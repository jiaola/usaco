import sys


def pour(day, a, first, second, lst):
    if day == 5:
        lst.append(a)
    else:
        if day == 1 or day == 3:  # Tuesday or Thursday
            for i in range(len(first)):
                first_copy = first.copy()
                second_copy = second.copy()
                bucket = first_copy.pop(i)
                second_copy.append(bucket)
                lst = pour(day+1, a + bucket, first_copy, second_copy, lst)
        elif day == 2 or day == 4:  # Wed or Fri
            for i in range(len(second)):
                first_copy = first.copy()
                second_copy = second.copy()
                bucket = second_copy.pop(i)
                first_copy.append(bucket)
                lst = pour(day + 1, a - bucket, first_copy, second_copy, lst)
    return lst


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    first = [int(i) for i in input().split()]
    second = [int(i) for i in input().split()]
    lst = pour(1, 0, first, second, [])
    print(len(set(lst)))


if __name__ == "__main__":
    main('backforth')
