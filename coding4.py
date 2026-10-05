def flatten_list(items):
    result=[]

    for item in items:
        if isinstance(item,list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result

if __name__=="__main__":
    nums=[1,2,[3,4],[5,6,7],[8,[9]]]

    result=flatten_list(nums)
    print(result)
