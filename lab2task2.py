n1 = 1
n2 = 2
n3 = 0
s = 0
while n3 < 4000000:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    if n3 % 2 == 0:
        s += n3
print(s)