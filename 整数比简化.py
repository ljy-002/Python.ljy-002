class num():
    def hcf(x,y):
        if x>y:
            smaller=y
        else:
            smaller=x
        for i in range(1,smaller+1):
            if x%i==0 and y%i==0:
                hcf=i
        return hcf

def rat(num1,num2):
    big=num.hcf(num1,num2)
    print("前项和后项的最大公因数是",big)
    print(num1,":",num2,"=","(",num1,"/",big,")",":","(",num2,"/",big,")","=",int(num1/big),":",int(num2/big))
    print("你输入的比是：",num1,":",num2)
    print("化简后的比是：",int(num1/big),":",int(num2/big))

rat(int(input("比的前项：")),int(input("比的后项：")))

