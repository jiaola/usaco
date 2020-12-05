import sys

sys.stdin = open('mixmilk.in', 'r')
sys.stdout = open('mixmilk.out', 'w')

c1, m1 = map(int, input().split())
c2, m2 = map(int, input().split())
c3, m3 = map(int, input().split())

for i in range(33):
    p = min(m1, c2 - m2)
    m2 = m2 + p
    m1 = m1 - p

    p = min(m2, c3 - m3)
    m3 = m3 + p
    m2 = m2 - p

    p = min(m3, c1 - m1)
    m1 = m1 + p
    m3 = m3 - p

p = min(m1, c2 - m2)
m1 = m1 - p
m2 = m2 + p

print(str(m1))
print(str(m2))
print(str(m3))