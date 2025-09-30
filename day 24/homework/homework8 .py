subjects = ["მათემატიკა", "ინგლისური", "ფიზიკა", "ბიოლოგია", "გეოგრაფია"]

grades = [85, 90, 78, 92, 88]  # ქულები თითოეულ საგანში

total = 0
for grade in grades:
    total += grade

average = total / len(grades)

print("სემესტრული საშუალო ქულა:", average)