import random


def Sort(array):
    for i in range(1, len(array)):
        a = array[i]

        j = i - 1

        while j >= 0 and a < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = a


x = random.sample(range(1, 100), 20)
print("random array", x)
Sort(x)
print("asc order", x)
