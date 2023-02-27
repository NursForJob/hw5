import random

n = []
for i in range(50):
    n.append(i)
print(n)

Last = len(n) - 1
ResultOk = False
First = 0


def binarysearch(list_num, find, start, stop):
    if start > stop:
        return ResultOk
    else:
        middle = (start + stop) // 2
        if find == list_num[middle]:
            return middle
        elif find < list_num[middle]:
            return binarysearch(list_num,find,start,middle -1)
        else:
            return binarysearch(list_num, find, middle+1, stop)


find = 55

ans = binarysearch(n, find, First, Last)
if ans == False:
    print(f"Индекса {find} нету в списке ")
else:
    print(f"Индекс {find}  найден")