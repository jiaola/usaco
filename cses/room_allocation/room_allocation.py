from sys import stdin, stdout


def main(pname):
    n = int(input())
    r_v = []  # vacant rooms
    c_r = [0] * n  # customer room
    e = []
    max_rooms = 0
    for i in range(n):
        a, d = stdin.readline().split()
        e.append((int(a), False, i))  # in
        e.append((int(d), True, i))  # out

    e.sort()
    for evt in e:
        d, out, c_n = evt
        if out:
            r_v.append(c_r[c_n])
        else:
            if not r_v:  # no vacant room
                max_rooms += 1
                c_r[c_n] = max_rooms
            else:
                c_r[c_n] = r_v.pop()

    stdout.write(str(max_rooms) + '\n')
    stdout.write(' '.join([str(c_r[i]) for i in range(n)]))


if __name__ == "__main__":
    main('room')