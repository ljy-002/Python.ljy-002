#冒泡排序

lists=[]


def bubble_sort(nums):
    for i in range(len(nums)-1):  #这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  #j为列表下标
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums


def ask(outask):
    lists=[]
    while len(lists)>80:
        outask=int(input("你要排序哪几个数，回复“1”为加入数值，回复“2”为开始排序"))
        if outask==1:
            lists.append(outask)
            print("加入成功")
        elif outask==2:
            break
        else:
            print("您输入错误，请重新输入")


ask("排序")
print("正在排序……")
bubble_sort(lists)
print("排序完成")
