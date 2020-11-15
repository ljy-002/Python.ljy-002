import os

#重命名文件：
#os.rename(src, dst)

path="D:\套娃"
for i in range(int(input("你要几层套娃？"))-1):
    path+="\套娃"

os.makedirs(path,mode=0o770)