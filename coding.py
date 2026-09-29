import string

def word_frequency(text):
    text = "AI is powerful, and AI is useful!"
    text=text.lower()

    text=text.translate(str.maketrans("", "",string.punctuation))
    words=text.split()
    frequency={}
    for word in words:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1

    return frequency

def main():
    text=text = "AI is powerful, and AI is useful!"
    result=word_frequency(text)
    print(result)

if __name__=="__main__":
    main()
    