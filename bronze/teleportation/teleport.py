with open('teleport.in', 'r') as input:
    a, b, x, y = [int(i) for i in input.readline().strip().split()]

ax = abs(a - x)
ay = abs(a - y)
bx = abs(b - x)
by = abs(b - y)
ab = abs(a - b)

with open('teleport.out', 'w') as output:
    output.write(str(min([ab, ax+by, ay+bx])))