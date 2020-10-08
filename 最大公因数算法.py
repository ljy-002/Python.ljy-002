def hcf(x,y):
   #该函数返回两个数的最大公因数
   #获取最小值
   if x>y:
       smaller=y
   else:
       smaller=x
   for i in range(1,smaller+1):
       if x%i==0 and y%i==0:
           hcf=i
   return hcf


#版权
print("此程序由gitignore制作\n由©GITI保留所有权\n求最大公因数：")

#用户输入两个数字
num1=int(input("输入要算最大公因数的第一个数："))
num2=int(input("输入要算最大公因数的第二个数："))
print(num1,"和",num2,"的最大公约数为",hcf(num1, num2))

print("计算完毕\n版权由\n——©GITI-算法-最大公因数\n提供")
