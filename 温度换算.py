a = input("输入温度值，例如 30C 或 80F：")
if a[-1] in ['F','f']:
    C=(float(a[0:-1])-32)/1.8
    print("转成C是：","%.1fC"%(C))
elif a[-1] in ['C','c']:
    F=1.8*float(a[0:-1])+32
    print("转成F是：","%.1fF"%(F))
else:
    print("格式错误")


