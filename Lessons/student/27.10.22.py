


dict1={"Name": "Aigerim",
"Last name": "Kenzhebayeva",
"Age" : 15}

print(dict1["Name"])

print(dict1)
dict1["job"]="programmer"
print(dict1)
dict1["Age"]=18
print(dict1)
result1=dict1.get("email")
print(result1)
result1=dict1.get("email","@mail.ru")
print(result1)
result1=dict1.get("Name","@mail.ru")
print(result1)
result2=dict1.setdefault("number", 123456)
print(result2)
print(dict1)
#создание копии словаря
dict2=dict1
print(dict1,dict2)
dict1["Last name"]="Table"
print(dict1,dict2)
dict3=dict1.copy()
print(dict1,dict3)

dict1.clear()
print(dict1)

keys1=dict3.keys()
print(keys1)

values1=dict3.values()
print(values1)

items1=dict3.items()
print(items1)

sort1=sorted(dict3)
print(sort1)



dict4={"things":"books"}
print(dict4)
result4=dict4.setdefault("numbers", 123)
print(result4)
print(dict4)

result5=dict4.setdefault("toys", ["cars", "dolls"])
print(result5)
print(dict4)

result6=dict4.get("toys")
print(result5)

del dict4["things"]
print(dict4)

