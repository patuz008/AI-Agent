
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import ollama

from vector import retriever

# define model and input prompt
MODEL = OllamaLLM(model="llama3.2")


# Template for the conversation
template = """
You are an Experting in answering Pizza Restaurant reviews:
Here is the conversation history: {reviews}
Question: {question}
"""
PROMPT = ChatPromptTemplate.from_template(template)
chain = PROMPT | MODEL

# result = chain.invoke({"reviews": [], "question": "where is the best pizza place"})
# print (result)

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (Type Exit to Quit): ")
    print("\n\n")
    if question == "Exit":
        break
    
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)


