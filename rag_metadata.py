def document_search(document,doc_type):
    result=[]
    for item in document:
        if doc_type.lower() in item["type"].lower():
            result.append(item)
        
    return result


documents = [
    {
        "id": 1,
        "text": "Python is used for AI development",
        "source": "python.pdf",
        "type": "technical"
    },
    {
        "id": 2,
        "text": "FastAPI is used to build APIs",
        "source": "fastapi.pdf",
        "type": "technical"
    },
    {
        "id": 3,
        "text": "Company leave policy allows 20 days",
        "source": "hr.pdf",
        "type": "policy"
    },
    {
        "id": 4,
        "text": "Employees can work remotely",
        "source": "hr_remote.pdf",
        "type": "policy"
    }
]

result=document_search(documents,"policy")
print(result)