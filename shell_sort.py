#coding=utf-8
import random
#定义三个常量用来表示下限、上限和数组长度
start = 1
stop = 1000
length = 10
#定义一个新数组存放随机数
list = []
def random_list(start, stop, length):
    for i in range(length):
        list.append(random.randint(start, stop))  #把生成的随机数插入到list
    return list

print("随机生成的数组为：")
print(random_list(start,stop,length))
print("排序后的数组为：")

# 希尔排序length=len(seq)
num = 0
while num <= length / 3:
    num = num * 3 + 1
while num >= 1:
    for i in range(num,length):
        tmp = list[i]
        for j in range(i,0,- num):
            if tmp < list[j - num]:
                list[j] = list[j - num]
            else:
                j += num
                break
        list[j - num] = tmp
    num //= 3
print(list)


#时间复杂度：O(n^1.3)
#空间复杂度：0(1)