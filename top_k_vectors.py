query = [1, 2, 3]

documents = [
    {"id": 1, "embedding": [1, 2, 3]},
    {"id": 2, "embedding": [2, 4, 6]},
    {"id": 3, "embedding": [1, 0, 0]},
    {"id": 4, "embedding": [3, 2, 1]}
]

result = retrieve_top_k(query, documents, 2)
print(result)