def num(a,b,c,d):
    print("⠀⠀⠀",a,":",b,"=",c,":",d)
    if a=="x":
        b,c,d=int(b),int(c),int(d)
        print("解：",d,a,"=",b,"*",c)
        print("⠀⠀⠀⠀",a,"=",b*c,"/",d)
        print("⠀⠀⠀⠀⠀⠀",a,"=",int(b*c/d))
    elif b=="x":
        a,c,d=int(a),int(c),int(d)
        print("解：",c,b,"=",a,"*",d)
        print("⠀⠀⠀⠀",b,"=",a*d,"/",c)
        print("⠀⠀⠀⠀⠀⠀",b,"=",int(a*d/c))
    elif c=="x":
        a,b,d=int(a),int(b),int(d)
        print("解：",b,c,"=",a,"*",d)
        print("⠀⠀⠀⠀",c,"=",a*d,"/",b)
        print("⠀⠀⠀⠀⠀⠀",c,"=",int(a*d/b))
    elif d=="x":
        a,b,c=int(a),int(b),int(c)
        print("解：",a,d,"=",b,"*",c)
        print("⠀⠀⠀⠀",d,"=",b*c,"/",a)
        print("⠀⠀⠀⠀⠀⠀",d,"=",int(b*c/a))
    else:
        print("输入错误")


print("注：未知数用“x”表示")
q1=input("左面比的前项：")
q2=input("左面比的后项：")
h1=input("右面比的前项：")
h2=input("右面比的后项：")

num(q1,q2,h1,h2)

