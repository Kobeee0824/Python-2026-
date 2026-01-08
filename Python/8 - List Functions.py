lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.extend(lucky_numbers)#durugtong yung lucky_numbers list sa friends list
print(friends)

friends.append("Creed")#daragdag ng element sa list sa dulo
print(friends)

friends.insert(1, "Kelly")#nadagdag si kelly sa index 1 then umurong yung index number ng list
print(friends)

friends.remove("Jim")#remove si Jim sa list
print(friends)

friends.clear()#empty yung list
print(friends)

friends.pop()#tanggal last element
print(friends)

print(friends.index("Kevin"))#display index number ng specific element

friends.sort()#arrange alphabetically (ascending kapag numbers ang elements)
print(friends)

friends.reverse()#reverse yung order ng elements sa list
print(friends)

friends2 = friends.copy()#copy yung list 
print(friends2)