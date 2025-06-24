value = 5
while value > 0:
    print(value)
    value -=1

print("---for in루프---")
lst = [100, "apple", 3.14]
for item in lst:
    print(item, type(item))

d= {"apple":100, "kiwi":200}
for k,v in d.items():
    print(k,v)

lst=list(range(1.11))
print(lst)
print([i**2 ofr i in lst if i>5])

