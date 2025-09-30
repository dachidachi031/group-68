# სია
items = ["მარწყვი,ალუბალი,ატამი,ქლიავი,ანანასი"]

# append - ბოლოს ამატებს
items.append("ვაშლი")
items.append("ბანანი")

# insert - ჩასმა კონკრეტულ ადგილზე
items.insert(1, "მსხალი")

# len - რაოდენობა
print("სიგრძე:", len(items))

# remove - წაშლა სახელით
items.remove("ბანანი")

# pop - წაშლა ინდექსით
items.pop(0)

print("საბოლოო სია:", items)