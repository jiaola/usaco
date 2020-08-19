import sys

sys.stdin = open('shell.in', 'r')
sys.stdout = open('shell.out', 'w')

def check(l, c, a, b, g):
    if l == a:
        l = b
    elif l == b:
        l = a
    if l == g:
        c = c + 1
    return l, c

n = int(input())
l1 = 1
l2 = 2
l3 = 3
c1 = c2 = c3 = 0
for i in range(n):
    a, b, g = [int(j) for j in input().split()]
    l1, c1 = check(l1, c1, a, b, g)
    l2, c2 = check(l2, c2, a, b, g)
    l3, c3 = check(l3, c3, a, b, g)

print(max(c1, c2, c3))



    
        