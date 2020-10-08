a=[1, 2, 3]
b=[4, 5, 6]
c=[4, 5, 6, 7, 8]

zipped=zip(a,b)     #打包为元组的列表
print(zipped)

nums=['flower','flow','flight']
for i in zip(*nums):
    print(i)
    for j in i:
        print(j)
        for k in j:
            print(k)
