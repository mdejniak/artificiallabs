import matplotlib.pyplot as plt

x, sub = plt.subplots()
a = [-3, 1, 2, -2,  3, -1]
sub.plot(a)

b = [2 - i for i in a]
sub.plot(b)

c = [(i/3)*2 + 1 for i in a]
sub.plot(c)

d = [i*i for i in a]
sub.plot(d)

e = [2**i for i in a]
sub.plot(e)

f = [(2**i)-(i**3) for i in a]
sub.plot(f)

plt.show()