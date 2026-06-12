Built to replicate that one deeply human-like, chronically online friend who is always chilling in your Discord server at 3:00 AM, 
this chatbot strips away the boilerplate robotic politeness. Instead of asking "How may I assist you today?", it delivers lowkey sarcastic,
incredibly laid-back, and highly relatable responses.

The Tech Stack :

Framework: Streamlit
LLM : Groq Cloud API (llama-3.3-70b-versatile) — delivers lightning-fast, near-instant chat responses.
Language: Python

Getting Started

1. Clone the Repository

3. Install Dependencies
Make sure you have Python installed, then run:
pip install streamlit groq

4. Set Up Your API Secrets
Streamlit looks for secrets in a hidden folder. Create a .streamlit directory and a secrets.toml file inside it:
mkdir .streamlit
touch .streamlit/secrets.toml

Open .streamlit/secrets.toml and add your Groq API key:
GROQ_API_KEY = "API KEY HERE"

4. Run the Application
streamlit run app.py
