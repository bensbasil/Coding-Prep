def cosine_similarity(vector1, vector2):

    # 1. Calculate dot product
    dot_product = 0

    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]

    # 2. Calculate magnitude of vector1
    magnitude1 = 0

    for value in vector1:
        magnitude1 += value ** 2

    magnitude1 = magnitude1 ** 0.5

    # 3. Calculate magnitude of vector2
    magnitude2 = 0

    for value in vector2:
        magnitude2 += value ** 2

    magnitude2 = magnitude2 ** 0.5

    # 4. Calculate cosine similarity
    similarity = dot_product / (magnitude1 * magnitude2)

    return similarity


vector1 = [1, 2, 3]
vector2 = [2, 4, 6]

result = cosine_similarity(vector1, vector2)

print(result)