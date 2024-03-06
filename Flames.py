name01 = input("Enter the first name: ")
name02 = input("Enter the partner's name: ")
name1 = list(name01.lower().replace(" ", ""))
name2 = list(name02.lower().replace(" ", ""))
name1_copy = name1.copy()
name2_copy = name2.copy()

relationships = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]

for i in name1_copy:
    if i in name2_copy:
        name1.remove(i)
        name2.remove(i)

unique_elements = name2 + name1
count = len(unique_elements)

index = count % len(relationships)
if index >= 0:
    right = relationships[index:] 
    left = relationships[:index]  
    relationships = right + left

print(name01, '&', name02, "have", relationships[0], "relationship")
