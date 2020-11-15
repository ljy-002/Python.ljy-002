import os
import sys
import time

for i in range(3):
    fp="D:\测试\时间.log"
    with open(fp,'w',encoding='utf-8') as fn:   #如果文件存在时，先进行清空，实现对一个文件重复写
        pass
    while True:
        with open(fp,'a+',encoding='utf-8') as fn:
            fn.write(time.strftime("%Y-%m-%d %H:%M:%S")+" hello world!\n")
        fs=round(os.path.getsize(fp)/float(1024*1024),2)  #将文件大小的单位转换成MB
        if fs>=2:    #如果文件大小超过2MB时，重新写入另一个文件
            break