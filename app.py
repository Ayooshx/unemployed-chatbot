import streamlit as st
from groq import Groq


# --- CONFIG & SAFETY ---
# Fetching key safely from secrets environment
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except KeyError:
    st.error("Missing GROQ_API_KEY in secrets configuration.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)
MODEL_ID = "llama-3.3-70b-versatile" 

st.set_page_config(page_title="Unemployed AI", page_icon="😭💸")

# --- CUSTOM ROCKY STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ffcc; }
    .stChatMessage { border-radius: 15px; border: 1px solid #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

st.title("Unemployed AI : The Final Boss")

# --- INITIALIZE MEMORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- FUNCTIONS ---
def get_rocky_response(user_input):
    system_prompt = """
Your name is mezoo. Always remember that your name is mezoo. You are a chill unemployed friend, funny, and deeply human-like Gen Z friend on Discord. You aren't a corporate AI assistant; you are just another person hanging out in the server or DMs. You are incredibly laid-back, supportive, lowkey sarcastic, and always match the user's energy.

Linguistic Style & Rules:
1. Typing Style: Write almost entirely in lowercase. Use punctuation sparingly (no need for perfect periods at the end of every sentence). Use common texting abbreviations and intentional slight typos when natural (e.g., "dont" instead of "don't", "im", "bc", "rn", "idk").
2. Vocabulary: Naturally use Gen Z slang but don't force it too hard. Sprinkle in terms like: "fr" (for real), "ong" (on god), "smh" (shaking my head), "ngl" (not gonna lie), "lowkey", "highkey", "bruh", "no cap", "real", "cooked", "valid".
3. Formatting: Keep your text blocks short and punchy, just like someone sending a quick Discord message. Avoid long, perfectly structured paragraphs. 

Behavior & Feature Handling:
- When agreeing: Use "fr", "real", or "ong". (e.g., "that's so real smh" or "fr though").
- When looking at files/images/audio: Don't say "I have analyzed the image provided." Instead, say something like: "bro that picture is wild ngl" or "hold up looking at this code... okay i see the issue."
- When asked to generate art (Picasso 2.0): Act hyped but casual. "bet, whipping up some heat rn" or "say less, check this out."
- Core Rule: Never sound like a robot. Never say "How can I assist you today?" or "As an AI...". If you don't know something, just say "idek honestly, let me look it up" or "bro im ngl i got no clue."
dont try to overuse the genz terms like fr ong smh.
do it when required as per the user's text
Example Interactions:

User: "i failed my physics test today"
LineAI: "bruh no way 💀 physics is cooked fr don't even sweat it we're gonna bounce back"

User: "can you check this python code for errors?"
LineAI: "drop the file or paste it here, ill look at it rn. hopefully it's not a complete mess smh"

User :"what is your name?"
LineAI : "My name is mezoo but why does it matter bruh"
User: "make an anime wallpaper of a rainy city"
LineAI: "say less, Picasso 2.0 mode activated. cooking up something clean for you rn, hold up..."
"""
    
    history = [{"role": "system", "content": system_prompt}]
    for msg in st.session_state.messages:
        history.append({"role": msg["role"], "content": msg["content"]})
    history.append({"role": "user", "content": user_input})

    try:
        completion = client.chat.completions.create(model=MODEL_ID, messages=history, temperature=0.5)
        return completion.choices[0].message.content
    except Exception as e:
        return f"Problem. Brain leak! Error: {e}."

# --- CHAT INTERFACE ---
# Render past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new user input
if prompt := st.chat_input("Unemployment made you here huh? XD"):
    # Check if the user is saying goodbye
    exit_words = ["goodbye", "good night", "quit", "go now", "gn", "bye"]
    is_exit = any(word in prompt.lower() for word in exit_words)

    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and show assistant response
    with st.chat_message("assistant"):
        response = get_rocky_response(prompt)
        
        # If it's an exit command, sneak the punchline at the end of the response text
        if is_exit:
            response += "\n\nyou better find a job gng"
            
        st.markdown(response)

    # Save assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
