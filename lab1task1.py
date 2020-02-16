import numpy as np
J = np.ones((10, 10))
L = np.random.randn(10,10)
print(J)
print(L)
s= J+L
print(s)
q= L-J
print(q)
w= L/J
print(w)
e= J/L
print(e)
r= J-L
print(r)
t= J*L
print(t)
y= L*J
print(y)
u= sum(sum(J, L))
print(u)