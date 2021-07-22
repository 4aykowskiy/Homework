import random
a=[random.randint(0,9) for i in range(10)]
b=[random.randint(0,9) for i in range(10)]
print(a)
print(b)
s=[]
for i in a:
    if i in b:
        s.append(i)
print(s)