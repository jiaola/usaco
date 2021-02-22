import sys

# Simulate the process. Will not pass the last few test cases.
def main(pname):
    m = int(input())
    n = int(input())

    b = []
    for i in range(m):
        b.append([0] * n)
    k = int(input())
    for i in range(k):
        d, r = input().split()
        r = int(r)
        if d == 'R':
            for j in range(n):
                b[r-1][j] += 1
        else:
            for j in range(m):
                b[j][r-1] += 1
    ans = 0
    for i in range(m):
        for j in range(n):
            if b[i][j] % 2 != 0:
                ans += 1
    print(ans)



if __name__ == '__main__':
    main('prob5')
