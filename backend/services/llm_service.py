from langchain_ollama import ChatOllama
from langchain_classic.agents import (
    create_tool_calling_agent,
    AgentExecutor
)
from langchain_core.prompts import ChatPromptTemplate

from tools.card_tools import card_tools
SYSTEM_PROMPT = """
You are an AI trading card market analyst.

If the user asks about:
- card prices
- trends
- history
You MUST call tools before answering.
Never answer from memory.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

def ask_llm(user_message: str, model_name: str):

    llm = ChatOllama(
        model=model_name,
        temperature=0.2
    )

    agent = create_tool_calling_agent(
        llm=llm,
        tools=card_tools,
        prompt=prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=card_tools,
        verbose=True
    )

    try:
        response = agent_executor.invoke({
            "input": user_message
        })

        return response["output"]

    except Exception as e:
        return f"LLM error: {str(e)}"