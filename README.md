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

<img width="1366" height="768" alt="Unemployed AI · Streamlit - Google Chrome 6_12_2026 7_52_46 PM" src="https://github.com/user-attachments/assets/c45fd615-094c-4378-8766-9913dd962486" />
<img width="1366" height="768" alt="Unemployed AI · Streamlit - Google Chrome 6_12_2026 7_51_45 PM" src="https://github.com/user-attachments/assets/7c7732d0-2e38-4c36-83dc-51bd97f5df7a" />

