import openai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_embeddings(texts):
    embeddings = OpenAIEmbeddings()
    return [embeddings.embed_query(text) for text in texts]

def find_relevant_text_chunks(text_chunks, question, embeddings):
    question_embedding = generate_embeddings([question])[0]
    similarities = cosine_similarity([question_embedding], embeddings)
    most_relevant_chunk_index = np.argmax(similarities)
    return text_chunks[most_relevant_chunk_index]
