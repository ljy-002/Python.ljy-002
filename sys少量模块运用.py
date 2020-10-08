import time
import sys

a = time.time()
print(a)

b = sys.argv
print(b)

c = sys.base_prefix
print(c)

d = sys.builtin_module_names
print(d)

e = sys.copyright
print(e)

a1 = sys.dont_write_bytecode
print(a1)

a2 = sys.exec_prefix
print(a2)

a3 = sys.executable
print(a3)

#sys.path.append("自定义模块路径")
sys.path.append("D:\PROG\李今越\李今越\你好\hello")


#sys.getdefaultencoding()
#获取系统当前编码,一般默认为ascii
a4 = sys.getdefaultencoding()
print(a4)

#sys.setdefaultencoding()
#设置系统默认编码，执行dir（sys）时不会看到这个方法，在解释器中执行不通过，可以先执行reload(sys)，在执行 setdefaultencoding(‘utf8’)，此时将系统默认编码设置为utf8。（见设置系统默认编码 ）
a5 = sys.setdefaultencoding()
print(a5)


