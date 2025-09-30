import random

numbers = []
for i in range(20):
    numbers.append(random.randint(1, 100))

print("სრული სია:", numbers)

even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)

print("ლუწი რიცხვები:", even_numbers)