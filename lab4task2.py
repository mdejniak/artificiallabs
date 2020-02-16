x = ("I like artificial intelligence")
print(x)
z = x.replace(" ", "")
ngram_len = 3
d = dict()
a = []
if (len(z) % 3 > 0) & (ngram_len % 3 == 0):
    del a[-1]
for letter in range(len(z))[::ngram_len]:
    abc = z[letter] + z[letter + 1] + z[letter + 2]
    a.append(abc)
print(a)
for ngram in a:
    if ngram in d:
        d[ngram] = d[ngram] + 1
    else:
        d[ngram] = 1
print(d)