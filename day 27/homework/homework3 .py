print("გამარჯობა, მსოფლიო!")

name = input("შეიყვანე შენი სახელი: ")
print("გამარჯობა,", name)

x = [10, 20, 30]
print(len(x))

a = 5
print(type(a))

x = "5"
print(int(x) + 2)
print(float(x) + 0.5)
print(str(10) + " ლარი")

for i in range(5):
    print(i)

nums = [1, 2, 3, 4]
print(sum(nums))

nums = [4, 7, 1, 9]
print(max(nums))
print(min(nums))

nums = [5, 2, 9, 1]
print(sorted(nums))
print(sorted(nums, reverse=True))

print(list("abc"))
print(tuple([1, 2, 3]))
print(set([1, 2, 2, 3]))
print(dict(name="დაჩი", age=16))

print(abs(-10))
print(round(3.7))
print(round(3.14159, 2))
print(pow(2, 3))

help(print)

num = 10
print(id(num))

print(bool(1))
print(bool(0))

values = [True, False, True]
print(all(values))
print(any(values))

names = ["დაჩი", "გიო", "ნიკა"]
ages = [16, 17, 15]
combined = list(zip(names, ages))
print(combined)

fruits = ["ვაშლი", "მსხალი", "ატამი"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

nums = [1, 2, 3, 4]
print(list(reversed(nums)))