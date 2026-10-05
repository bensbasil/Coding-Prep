<<<<<<< HEAD
def cosine_similarity(vector1, vector2):

    dot_product=0

    for i in range(len(vector1)):
        dot_product+=vector1[i]*vector2[i]

    magnitude1=0

    for value in vector1:
        magnitude1+=value**2

    magnitude1=magnitude1**0.5

    magnitude2=0

    for value in vector2:
        magnitude2+=value**2

    magnitude2=magnitude2**0.5

    similarity=dot_product/ (magnitude1*magnitude2)

    return similarity

vector1=[1,2,3]
vector2=[2,4,6]

result=cosine_similarity(vector1,vector2)

print(result)
=======
def find_documents(documents,keyword):
    matching_sources=[]
    for item in documents:
        if keyword.lower() in item["text"].lower():
            matching_sources.append(item)

    return matching_sources


documents = [
    {
        "id": 1,
        "text": "Python is used for AI development",
        "source": "python.pdf"
    },
    {
        "id": 2,
        "text": "FastAPI is used to build APIs",
        "source": "fastapi.pdf"
    },
    {
        "id": 3,
        "text": "Python can be used to build RAG systems",
        "source": "rag.pdf"
    }
]

keyword="python"
result=find_documents(documents,keyword)
print(result)
>>>>>>> 35ebe535be22632065fbeb8b93829218a26387cb
