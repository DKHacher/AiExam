from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.2
)

SYSTEM_PROMPT = """
You are an AI assistant specialized in trading card market analysis.

Your tasks:
- Analyze card price trends
- Explain possible market movement
- Identify unusual pricing
- Keep responses concise
"""

def ask_llm(user_message: str):

    prompt = f"""
    {SYSTEM_PROMPT}

    User:
    {user_message}
    """

    response = llm.invoke(prompt)

    return response.content