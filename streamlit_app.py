import streamlit as st
from bot.query_engine import handle_query

st.set_page_config(page_title="Telecom Bot", page_icon="📱")

st.title("📱 Telecom Bot")
st.write("Ask anything about telecom plans — pricing, validity, data, benefits, and more.")

st.markdown("---")

# User input
user_query = st.text_input("Ask your telecom question:")

if st.button("Get Answer"):
    if user_query.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = handle_query(user_query)
            st.success("Here’s your answer:")
            st.write(response)

st.markdown("---")
st.caption("Powered by FAISS + Sentence Transformers + Ollama (Gemma 3)")