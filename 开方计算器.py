x=int(input("请输入一个要做开方运算的数字："))
i=0

const=0

while i**2<x:
    i+=1
    const+=1

while i**2<x:
    i+=0.01
    const+=1

print("开方结果：%f"%(i))
