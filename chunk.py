def chunk_text(text, chunk_size):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


text = "AI is changing the world and Python is widely used for building AI applications"

result = chunk_text(text, 5)

print(result)