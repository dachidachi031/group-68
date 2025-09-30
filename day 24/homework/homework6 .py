import random

names = ["ნიკა", "გიო", "საბა", "ტარიელი", "ლუკა", "დანიელი", "დათო"]
random_names = random.sample(names, 5)  

print("სია:", random_names)

my_name = "დაჩი"

if my_name in random_names:
    print(my_name)
else:
    print("not found")
