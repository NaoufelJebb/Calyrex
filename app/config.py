from os import environ
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

OLLAMA_CHAT_LLM = environ.get("OLLAMA_CHAT_LLM", "gemma:2b")
OLLAMA_SERVE_PORT = environ.get("OLLAMA_SERVE_PORT", 11434)
OLLAMA_CODE_LLM = environ.get("OLLAMA_CODE_LLM", "")
