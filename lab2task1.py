import numpy as geek

def invertList(list):
    for i in range(1, len(list)):
        list.insert(i-1, list.pop(len(list)-1))


list=[]
list_len = int(input("give lenght of list"))
for i in range(list_len):
    value = int(input("give value"))
    list.append(value)
print("random list", list);
invertList(list)
print("reverse", list)