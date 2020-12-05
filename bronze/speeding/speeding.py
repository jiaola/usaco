import sys

def main():
    sys.stdin = open('speeding.in', 'r')
    sys.stdout = open('speeding.out', 'w')

    n, m = [int(i) for i in input().split()]
    n_seg = []
    n_speed = []
    m_seg = []
    m_speed = []
    for i in range(n):
        s, sp = [int(i) for i in input().split()]
        n_seg.append(s)
        n_speed.append(sp)
    for i in range(m):
        s, sp = [int(i) for i in input().split()]
        m_seg.append(s)
        m_speed.append(sp)

    l_n = 0
    l_m = 0
    s_n = 0
    s_m = 0
    f = 0
    while l_n < 100 or l_m < 100:
        if l_n > l_m:
            l_m += m_seg.pop(0)
            s_m = m_speed.pop(0)
        elif l_n < l_m:
            l_n += n_seg.pop(0)
            s_n = n_speed.pop(0)
        else:
            l_n += n_seg.pop(0)
            s_n = n_speed.pop(0)
            l_m += m_seg.pop(0)
            s_m = m_speed.pop(0)
        if l_m > 0 and l_n > 0:
            f = max(f, s_m - s_n)

    print(f)

if __name__ == "__main__":
    main()
