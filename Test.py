a = [15, 30, 45, 60, 90]
b = [(a[i], a[i+1]) for i,_ in enumerate(a) if i < len(a) - 1]
c = [15, 30, 45, 60, 90]
d = {}
print(b)
for i, element in enumerate(b):
    d[element] = c[i]

print(d)

a1 = 50
for key, value in d.items():
    if a1 == 90:
        if key[1] == 90:
            print(value)
    if (key[0] <= a1 and a1 < key[1]):
        print(value)

t = []
t.append([1,3,4,5,7])
t.append([2,6,8,0])

print(t[0][1])

for i in range(3):
    print(i)