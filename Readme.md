# Build a Python AI Agent with the Python

This project showcases a simple AI Agent using the Ollama LLM, Langchain,  Python. 


## Project Files

| File | Description |
|------|-------------|
| `aiAgent.py` | Implements a chatbot using OllamaLLM and LangChain to answer pizza restaurant review queries, retrieving relevant reviews from the vector store and generating responses. |
| `vector.py` | Loads restaurant reviews from a CSV, creates document embeddings using OllamaEmbeddings, and stores them in a Chroma vector store for retrieval. It checks if the database exists and adds documents if needed. |
