def rem_duplicates(numbers):
    seen={}
    result=[]
    
    for num in numbers:
        if num not in seen:
            seen[num]=True
            result.append(num)

        
    return result

if __name__=="__main__":
    nos=[1,2,3,6,1,4,5,3,2,7,8,9,7]
    result=rem_duplicates(nos)
    print(result) 