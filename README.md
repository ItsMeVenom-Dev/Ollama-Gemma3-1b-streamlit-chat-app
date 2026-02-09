# Ollama Streamlit Chat App

A simple Streamlit-based chat application using a locally running LLM via Ollama and LangChain.

## Features
- Local LLM inference using Ollama (gemma3)
- LangChain prompt → LLM → output parser pipeline
- Simple chat UI using Streamlit
- No external API cost

## Tech Stack
- Python
- LangChain
- Ollama
- Streamlit

## Setup Instructions

1. Install Ollama  
2. Pull model:
   ollama pull gemma3:1b

3. Install dependencies:
   pip install -r requirements.txt

4. Run app:
   streamlit run app.py
