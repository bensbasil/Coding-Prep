def list_add(list1, list2):
    result=[]
    for i in range(len(list1)):
        result.append(list1[i]+list2[i])

    result.extend(list2[len(list1):])
    return result

list1=[1,2,3,4,5,6]
list2=[3,6,7,2,6,9,12,4,5,6,7,9]



print(list_add(list1,list2))