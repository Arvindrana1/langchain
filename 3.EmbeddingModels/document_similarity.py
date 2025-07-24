import google.generativeai as genai
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

# Load environment variables from .env file
load_dotenv()

# Configure the genai library with the API key from the environment
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

# Use genai.embed_content to create embeddings
# Note the use of 'task_type' to specify the purpose of the embedding
doc_embeddings_result = genai.embed_content(
    model='models/embedding-001',
    content=documents,
    task_type="RETRIEVAL_DOCUMENT"
)

query_embedding_result = genai.embed_content(
    model='models/embedding-001',
    content=query,
    task_type="RETRIEVAL_QUERY"
)

# Extract the embedding vectors from the result dictionaries
doc_embeddings = doc_embeddings_result['embedding']
query_embedding = query_embedding_result['embedding']


# The similarity calculation logic remains exactly the same
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(f"Query: {query}")
print(f"Most similar document: {documents[index]}")
print(f"Similarity score: {score:.4f}")