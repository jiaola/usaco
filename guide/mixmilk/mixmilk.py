import sys

sys.stdin = open('mixmilk.in', 'r')
sys.stdout = open('mixmilk.out', 'w')

b1, m1 = [int(i) for i in input().split()]
b2, m2 = [int(i) for i in input().split()]
b3, m3 = [int(i) for i in input().split()]
c = 0
while True:
    if m1 + m2 >= b2: 
        m1 = m1 + m2 - b2 
        m2 = b2 
    else:
        m2 = m1 + m2
        m1 = 0      
    c += 1
    if c == 100:
        break   
    if m2 + m3 >= b3:
        m2 = m2 + m3 - b3 
        m3 = b3 
    else:
        m3 = m2 + m3 
        m2 = 0  
    c += 1
    if c == 100:
        break         
    if m3 + m1 >= b1:
        m3 = m3 + m1 - b1
        m1 = b1 
    else:
        m1 = m3 + m1
        m3 = 0
    c += 1
    if c == 100:
        break   

print(m1)
print(m2)
print(m3)
