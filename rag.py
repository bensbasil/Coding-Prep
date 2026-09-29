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