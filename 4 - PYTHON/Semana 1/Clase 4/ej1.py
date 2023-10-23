import collections


def duplicate_numbers(list):
    aux_list = []
    for i in list:
        if list.count(i) == 1:
            aux_list.append(i)
        elif list.count(i) > 1 and i not in aux_list:
            aux_list.append(i)
            list.remove(i)
    aux_list.sort()
    list=[]
    return aux_list


list = [1,2,2,2,2,2,3,4,5,1231,8,1,2,34,1]
print(duplicate_numbers(list))
