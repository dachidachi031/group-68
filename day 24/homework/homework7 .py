fruits = ["ვაშლი", "ბანანი", "მანგო", "ანანასი", "სტაფილო", "მარწყვი", "ქლიავი", "კივი", "ნაშუა", "ქოქოსი", "ალუბალი", "ატამი"]

top5_priority = ["ვაშლი", "მარწყვი", "ბანანი", "ალუბალი", "ატამი"]

filtered_fruits = []

for fruit in fruits:
    if fruit in top5_priority:
        filtered_fruits.append(fruit)

final_list = []
i = 0
while i < len(top5_priority):
    if top5_priority[i] in filtered_fruits:
        final_list.append(top5_priority[i])
    else:
        if len(filtered_fruits) > 0:
            filtered_fruits.pop(0)
    i += 1

print("Top 5 ხილი პრიორიტეტულად:", final_list)