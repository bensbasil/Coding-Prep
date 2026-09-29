
query = [1, 2, 3]

documents = [
    {"id": 1, "embedding": [1, 2, 3]},
    {"id": 2, "embedding": [2, 4, 6]},
    {"id": 3, "embedding": [1, 0, 0]},
    {"id": 4, "embedding": [3, 2, 1]}
]


def cosine_similarity(vector1, vector2):

    # Calculate dot product
    dot_product = 0

    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]

    # Calculate magnitude of vector1
    magnitude1 = 0

    for value in vector1:
        magnitude1 += value ** 2

    magnitude1 = magnitude1 ** 0.5

    # Calculate magnitude of vector2
    magnitude2 = 0

    for value in vector2:
        magnitude2 += value ** 2

    magnitude2 = magnitude2 ** 0.5

    # Calculate cosine similarity
    similarity = dot_product / (magnitude1 * magnitude2)

    return similarity


def retrieve_top_k(query, documents, k):

    results = []

    # Calculate similarity for every document
    for document in documents:

        embedding = document["embedding"]

        similarity = cosine_similarity(query, embedding)

        results.append({
            "id": document["id"],
            "score": similarity
        })

    # Sort highest score to lowest score
    results.sort(key=lambda x: x["score"], reverse=True)

    # Return top K documents
    return results[:k]


result = retrieve_top_k(query, documents, 2)

print(result)