"""Annotated example for comparing text similarity with OpenAI embeddings.

Requirements:
- Set `OPENAI_API_KEY` in your environment before running the script
"""

import json
import math
import os
from urllib import error, request


def get_embedding(text, model="text-embedding-3-small"):
    """Request an embedding vector for a single text string."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Set OPENAI_API_KEY before running this script.")

    payload = json.dumps(
        {
            "model": model,
            "input": text,
        }
    ).encode("utf-8")

    req = request.Request(
        "https://api.openai.com/v1/embeddings",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with request.urlopen(req) as response:
            body = json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI API request failed: {details}") from exc

    return body["data"][0]["embedding"]


def cosine_similarity(vec1, vec2):
    """Return cosine similarity where higher values mean more similar meaning."""
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must have the same length.")

    # Compute cosine similarity with built-in math so no third-party packages are needed.
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(value * value for value in vec1))
    magnitude2 = math.sqrt(sum(value * value for value in vec2))

    # Guard against invalid input that would make the denominator zero.
    if magnitude1 == 0 or magnitude2 == 0:
        raise ValueError("Cosine similarity is undefined for zero-length vectors.")

    return dot_product / (magnitude1 * magnitude2)


# These sample texts let you compare related and unrelated meanings.
texts = [
    "I love programming in Python",
    "Python coding is amazing",
    "I enjoy cooking Italian food",
    "Software development with Python",
]

# Generate one embedding per text so we can compare them pairwise.
embeddings = [get_embedding(text) for text in texts]


# Compare each unique pair once; `i < j` avoids duplicate comparisons.
for i, text1 in enumerate(texts):
    for j, text2 in enumerate(texts):
        if i < j:
            similarity = cosine_similarity(embeddings[i], embeddings[j])
            print(f"'{text1}' vs '{text2}': {similarity:.3f}")
