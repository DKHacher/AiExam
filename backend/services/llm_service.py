from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.2
)

SYSTEM_PROMPT = """
You are an AI assistant specialized in trading card analysis.
"""

def ask_llm(user_message: str, card_data: str):

    prompt = f"""
    {SYSTEM_PROMPT}

    Card data:
    {card_data}

    User question:
    {user_message}
    """

    response = llm.invoke(prompt)

    return response.content