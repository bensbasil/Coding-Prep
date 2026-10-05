
def retrieval(documents,keyword,k):
    result=[]
    for item in documents:
        if keyword.lower() in item["text"].lower():
            result.append(item)
            if len(result)==k:
                break
    return result


documents = [
    {"id": 1, "text": "Python is used for AI development"},
    {"id": 2, "text": "Python is popular for machine learning"},
    {"id": 3, "text": "FastAPI is used to build APIs"},
    {"id": 4, "text": "Python can be used to build RAG systems"}
]


result=retrieval(documents,"python",2)
print(result)
    