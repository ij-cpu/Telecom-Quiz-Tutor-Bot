import faiss
from sentence_transformers import SentenceTransformer
from data.plans import telecom_plans

model = SentenceTransformer("all-MiniLM-L6-v2")

def plan_to_text(plan):
    return (
        f"Provider: {plan['provider']}, "
        f"Price: {plan['price']}, "
        f"Validity: {plan['validity']}, "
        f"Data: {plan['data']}, "
        f"Calls: {plan['calls']}, "
        f"Extras: {plan['extras']}"
    )

plan_texts = [plan_to_text(p) for p in telecom_plans]
embeddings = model.encode(plan_texts)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def search_plans(query, k=2):
    query_embedding = model.encode([query])
    _, indices = index.search(query_embedding, k)
    return [telecom_plans[i] for i in indices[0]]