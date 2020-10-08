temp_1=0
temp_2=0
temp_3=''
zhishushulie=[]


def tast(number):
    global zhishushuliebiao
    temp_2=2
    temp_3='yes'
    for __count in range(number-2):
        if (number%temp_2==0):
            temp_3='no'
        temp_2+=1
    if (temp_3=='yes'):
        zhishushuliebiao.append(number)


def Prime_number(Prime):
    global zhishushuliebiao
    temp_1=2
    for __count in range(Prime):
        tast(temp_1)
        temp_1+=1
    print(zhishushuliebiao)


Prime_number(int(input("你要算到质数第几位：")))
