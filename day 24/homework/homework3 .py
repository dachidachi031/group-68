guests = ["ნიკა", "გიო", "საბა", "ტარიელი", "ლუკა", "დანიელი", "დათო"]
print("1) თავდაპირველი სია:", guests)

removed = []
removed.append(guests.pop(1))
removed.append(guests.pop(2))

added = []
guests.append("გაბრიელი")
added.append("გაბრიელი")

guests.insert(2, "თემური")
added.append("თემური")

count = len(guests)

print("2) ამოკლებული ადამიანები:", removed)
print("3) დამატებული ადამიანები:", added)
print("4) რამდენი ადამიანი დარჩა სულ:", count)
print("5) საბოლოო სია:", guests)