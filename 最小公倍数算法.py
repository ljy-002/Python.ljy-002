def gcd(n1, n2):
    #最大公约数函数
    return gcd(n2,n1%n2) if n2>0 else n1


def lcm(n1, n2):
    #最低通用倍数
    return n1*n2//gcd(n1,n2)


#版权
print("此程序由gitignore制作\n由©GITI保留所有权\n求最小公倍数：")

#用户输入两个数字
num1=int(input("输入要算最小公倍数的第一个数："))
num2=int(input("输入要算最小公倍数的第二个数："))
print(num1,"和",num2,"的最小公倍数为",lcm(num1,num2))

print("计算完毕\n版权由\n——©GITI-算法-最小公倍数\n提供")
