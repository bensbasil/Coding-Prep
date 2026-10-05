def is_unique(text):
    frequency={}
    for char in text:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
        
    for char in text:
        if frequency[char]==1:
            return char
    
    return None

if __name__=="__main__":
    text="aaaabbcccddddfggg"
    result=is_unique(text)
    print(result)

