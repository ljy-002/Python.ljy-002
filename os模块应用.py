import os


#python读写,创建文件
#python中对文件、文件夹(文件操作函数)的操作需要涉及到os模块和shutil模块。

#得到当前工作目录，即当前Python脚本工作的目录路径:
os.getcwd()

#返回指定目录下的所有文件和目录名：
os.listdir()

#函数用来删除一个文件：
os.remove()

#删除多个目录：
os.removedirs()

#检验给出的路径是否是一个文件：
os.path.isfile()

#检验给出的路径是否是一个目录：
os.path.isdir()

#判断是否是绝对路径：
os.path.isabs()

#检验给出的路径是否真地存: 
os.path.exists()

#返回一个路径的目录名和文件名：
os.path.split()
#比如：os.path.split('/home/swaroop/byte/code/poem.txt') 
#结果：('/home/swaroop/byte/code', 'poem.txt')

#分离扩展名：
os.path.splitext()

#获取路径名：
os.path.dirname()

#获取文件名：
os.path.basename()

#运行shell(打开)命令: 
os.system()

#读取和设置环境变量：
os.getenv()
#与
os.putenv()

#给出当前平台使用的行终止符:
#Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
os.linesep

#指示你正在使用的平台：
#对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
os.name

#重命名：
os.rename(old, new)

#创建多级目录：
os.makedirs(r"c：\python\test")

#创建单个目录：
os.mkdir("test")

#获取文件属性：
os.stat(file)

#修改文件权限与时间戳：
os.chmod(file)

#终止当前进程：
os.exit()

#获取文件大小：
os.path.getsize(filename)


#文件操作：
os.mknod("test.txt")        #创建空文件
fp = open("test.txt", w)    #直接打开一个文件，如果文件不存在则创建文件

#运行速度有点慢，请耐心等待！！！！！！
#你的D盘会多出一张名为pkpk.gif的图片！！！！！！！
#绝对是我原创！！！！！
