"""
PROB: ride
LANG: PYTHON3
"""
with open('ride.in', 'r') as fin:
    lines = fin.read().splitlines()

comet, group = lines

def code(s):
    c = 1
    for i in s:
        c *= ord(i) - 64
    return c % 47

with open('ride.out', 'w') as fout:
    if code(comet) == code(group):
        fout.write('GO\n')
    else:
        fout.write('STAY\n')
