def FibSeq(n):
    sep=[]
    sep.append(1)
    sep.append(1)
    for i in range(2,n,1):
        sep.append(sep[i-1]+sep[i-2])
    return sep


print("假如你养殖小鸡，那么你从开始到第20天的小鸡数量分别是：")
print(FibSeq(20))