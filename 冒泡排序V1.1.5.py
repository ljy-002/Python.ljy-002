lists=[]

def bubble_sort(nums):
    for i in range((len(nums)-1)):
        for j in range(((len(nums)-i)-1)):
            if (nums[j]>nums[(j+1)]):
                nums[j],nums[(j+1)]=nums[(j+1)],nums[j]
    return nums


def ask(outask):
    lists=[]
    outask=0
    while True:
        outask=int(input('你要排序哪几个数，回复“1”为加入数值，回复“2”为开始排序'))
        if outask==1:
            outask=int(input('你要加入哪几个数？'))
            lists.append(outask)
            print('加入成功，你加入的数是', outask)
        elif outask==2:
            outask=lists
            break
        else:
            print('您输入错误，请重新输入')

try:
    print(bubble_sort(ask("")))
    print('排序完成')
except:
    print('排序失败，请重新尝试')
