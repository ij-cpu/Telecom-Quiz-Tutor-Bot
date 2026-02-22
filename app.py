from bot.query_engine import handle_query

print("📱 Telecom Plan Comparison Bot (type 'exit' to quit)\n")

while True:
    query = input("Ask your question: ")

    if query.lower() == "exit":
        print("Goodbye 👋")
        break

    answer = handle_query(query)
    print("\n🤖 Bot Response:")
    print(answer)
    print("-" * 50)