from embeddings.vector_store import search_plans, plan_to_text
from llm.gemma_client import ask_gemma

def handle_query(user_query):
    plans = search_plans(user_query)

    context = "\n".join([plan_to_text(p) for p in plans])

    return ask_gemma(user_query, context)