numbers = [12, 7, 9, 20, 15, 6, 8, 3]

odd_numbers = []
for n in numbers:
    if n % 2 != 0:
        odd_numbers.append(n)

sum_odd = 0
for n in odd_numbers:
    sum_odd += n

print("კენტი რიცხვები:", odd_numbers)
print("კენტების ჯამი:", sum_odd)