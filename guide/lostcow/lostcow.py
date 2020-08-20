import sys

def main():
    sys.stdin = open('lostcow.in', 'r')
    sys.stdout = open('lostcow.out', 'w')

    x, y = [int(i) for i in input().split()]
    n = 0
    s = 1
    d = 0 
    p = x
    while not (x < y <= p  or p <= y < x):        
        p_n = x + (2 ** n) * s
        d += abs(p_n - p)
        n += 1
        s = -s
        p = p_n
    d -= abs(p - y)
    print(d)

if __name__ == "__main__":
    main()
