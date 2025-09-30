numbers = [12, 7, 9, 20, 15, 6, 8, 3]

even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)

sum_even = 0
for n in even_numbers:
    sum_even += n

print("ლუწი რიცხვები:", even_numbers)
print("ლუწების ჯამი:", sum_even)