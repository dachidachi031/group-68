import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))

print("სრული სია:", numbers)

odd_numbers = []
for n in numbers:
    if n % 2 != 0:
        odd_numbers.append(n)

print("კენტი რიცხვები:", odd_numbers)
