import sys


def gen(chars, s, lst):
    if len(chars) == 0:
        lst.append(s)
    else:
        for j in range(len(chars)):
            new_chars = chars[0:j] + chars[j+1:]
            lst = gen(new_chars, s + chars[j], lst)
    return lst


def main(pname):
    # sys.stdin = open(pname + '.in', 'r')
    # sys.stdout = open(pname + '.out', 'w')
    chars = input()
    lst = gen(chars, '', [])
    lst = sorted(list(set(lst)))
    print(len(lst))
    print('\n'.join(lst))


if __name__ == "__main__":
    main('creating_string')
