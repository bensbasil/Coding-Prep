def sum_add(num,target):
    seen={}
    for i in range(len(num)):
        val=target-num[i]

        if val in seen:
            return[seen[val],i]

        seen[nums[i]]=i

    return[]

if __name__=="__main__":
    nums=[2,7,11,15]
    target=22

    print(sum_add(nums,target))