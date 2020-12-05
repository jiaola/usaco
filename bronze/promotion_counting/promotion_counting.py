lines = []
with open('promote.in') as input:
    for i in range(4):
        lines.append(input.readline().strip())

p = 0
pa = []
for i in range(3, 0, -1):
    n = list(map(int, lines[i].split()))
    p = n[1] - n[0] + p
    pa.append(p) 
pa = pa[::-1]
with open('promote.out', 'w') as output:
    for p in pa:
        output.write(str(p) + '\n')




