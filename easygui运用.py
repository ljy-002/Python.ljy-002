import sys
import easygui as g


if g.buttonbox(msg="你喜欢下面哪种水果?", title="", choices=("西瓜", "苹果", "草莓", "没有我喜欢的")):
    g.msgbox("不问你了，谢谢答题")

if g.ccbox("哥你上课么?", choices=("还要学！", "算了吧/(ㄒoㄒ)/~~")):
    g.msgbox("还是不学了，快睡觉吧！")
else:
    sys.exit(0)

xxh = g.enterbox(msg="请说出此时你的心里话", title="心里悄悄话")
print("你心里悄悄话是：", xxh)

g.buttonbox("大家说鸡蛋可爱吗?", image="D:\PROG\李今越\李今越\杂项\文件类型\Png Gif Jpg Jfif Tiff\25973507_200x118.gif",
            choices=("可爱", "不可爱", "财迷"))
