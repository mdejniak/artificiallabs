x = ("I am what I am")

w = x.split()
print(w)
d = dict()
for word in w:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
print(d)
