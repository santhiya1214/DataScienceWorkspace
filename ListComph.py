## List Comprehension
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
d=[]
print(a)
for n in a:
    if n%2==0:
        d.append(n)
print(d)