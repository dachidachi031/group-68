import random

lst = []
for i in range(15):
    lst.append(random.randint(1, 100))
print("სია:", lst)

# დაყოფა ორ ნაწილად
a = lst[:8]
b = lst[8:]
print(a)
print(b)

# დაყოფა სამ ნაწილად
x = lst[:5]
y = lst[5:10]
z = lst[10:]
print(x)
print(y)
print(z)

# დაყოფა ოთხ ნაწილად
m1 = lst[:4]
m2 = lst[4:8]
m3 = lst[8:12]
m4 = lst[12:]
print(m1)
print(m2)
print(m3)
print(m4)

# დაყოფა ხუთ ნაწილად
n1 = lst[:3]
n2 = lst[3:6]
n3 = lst[6:9]
n4 = lst[9:12]
n5 = lst[12:]
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

# პირველი 5 და ბოლო 7 ელემენტი
print("პირველი 5:", lst[:5])
print("ბოლო 7:", lst[-7:])

# უარყოფითი slicing
print("უარყოფითი slicing:", lst[-10:-5])