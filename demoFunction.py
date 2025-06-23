def setValue(newValue):
    x=newValue
    print("함수 내부:",x)


result=setValue(5)
print(result)

def swap(x,y):
    return y,x

result =swap(3,4)
print(result)

x=5
def func(a):
    return a+x

print(func(1))

def func2(a):
    x=10
    return a+x

print(func2(1))


def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM","EGG"))

g = lambda x,y: y*x
print(g(3, 4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())