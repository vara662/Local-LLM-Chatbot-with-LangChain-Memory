
import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="SYNORA AI",
    page_icon="🔴",
    layout="wide"
)


# ==========================================
# 2. CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg, #090909, #260505, #100202
    );
    color: white;
}

/* All normal text */

.stApp p,
.stApp h1,
.stApp h2,
.stApp h3,
.stApp label {
    color: white;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg, #160303, #380707, #100202
    );
    border-right: 1px solid #FF3333;
}

/* Brand card */

.brand-box {
    text-align: center;
    padding: 20px 10px;
    background: linear-gradient(
        135deg, #280505, #570909
    );
    border: 1px solid #FF3333;
    border-radius: 20px;
}

/* Simple AI logo */

.ai-logo {
    width: 75px;
    height: 75px;
    margin: 0 auto 12px auto;
    border-radius: 50%;
    background: linear-gradient(
        135deg, #FF7777, #B00000
    );
    box-shadow: 0 0 25px #FF3333;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 38px;
    font-weight: bold;
}

/* Main header */

.main-header {
    text-align: center;
    padding: 30px 20px;
    margin-bottom: 25px;
    background: linear-gradient(
        135deg, #240505, #510909, #240505
    );
    border: 1px solid #FF3333;
    border-radius: 22px;
    box-shadow: 0 0 25px rgba(255,30,30,0.2);
}

.main-title {
    font-size: 43px;
    font-weight: 900;
    letter-spacing: 5px;
    color: #FF4545;
    text-shadow: 0 0 15px #FF2222;
}

.subtitle {
    color: white;
    font-size: 17px;
}

/* Memory card */

.memory-card {
    background: linear-gradient(
        135deg, #350707, #610B0B
    );
    border: 1px solid #FF3333;
    border-radius: 15px;
    padding: 15px;
    margin-top: 15px;
}

/* Chat messages */

[data-testid="stChatMessage"] {
    background: rgba(75,10,10,0.85);
    border: 1px solid #B91C1C;
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 15px;
}

[data-testid="stChatMessage"] p {
    color: white !important;
}

/* Chat input */

[data-testid="stChatInput"] {
    background: white !important;
    border: 2px solid #FF3333 !important;
    border-radius: 15px !important;
}

[data-testid="stChatInput"] textarea {
    color: black !important;
    -webkit-text-fill-color: black !important;
    background: white !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #777777 !important;
    -webkit-text-fill-color: #777777 !important;
}

/* Buttons */

.stButton button {
    background: linear-gradient(
        90deg, #A80000, #FF3333
    ) !important;
    color: white !important;
    border: 1px solid #FF7777 !important;
    border-radius: 12px !important;
    font-weight: bold;
}

.stButton button p {
    color: white !important;
}

/* Expander */

[data-testid="stExpander"] {
    background: #270707;
    border: 1px solid #FF3333;
    border-radius: 12px;
}

[data-testid="stExpander"] p {
    color: white !important;
}

/* Footer */

.footer {
    text-align: center;
    color: #FF9999;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "history_store" not in st.session_state:
    st.session_state.history_store = {}


SESSION_ID = "synora_user"


# ==========================================
# 4. LOAD GEMMA MODEL
# ==========================================

@st.cache_resource
def load_llm():

    return ChatOllama(
        model="gemma3:1b",
        temperature=0.7
    )


# ==========================================
# 5. LANGCHAIN MEMORY
# ==========================================

def get_session_history(session_id):

    if session_id not in st.session_state.history_store:

        st.session_state.history_store[session_id] = (
            InMemoryChatMessageHistory()
        )

    return st.session_state.history_store[session_id]


# ==========================================
# 6. CREATE CHATBOT
# ==========================================

def create_chatbot(llm):

    prompt = ChatPromptTemplate.from_messages([

        (
            "system",
            """
            You are SYNORA AI, a friendly and intelligent
            personal AI assistant.

            Instructions:
            1. Give clear and useful answers.
            2. Remember previous conversations.
            3. Answer in simple English.
            4. Be friendly and helpful.
            5. Avoid unnecessary repetition.
            """
        ),

        MessagesPlaceholder(variable_name="history"),

        ("human", "{input}")

    ])

    chain = prompt | llm

    chatbot = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )

    return chatbot


# ==========================================
# 7. SIDEBAR BRAND LOGO
# ==========================================

st.sidebar.html("""
<div class="brand-box">

    <div class="ai-logo">✦</div>

    <h2 style="
        color:#FF4545;
        letter-spacing:3px;
        font-size:27px;
    ">
        SYNORA AI
    </h2>

    <p style="color:white;">
        Your Personal AI Assistant
    </p>

    <p style="
        color:#FF7777;
        font-size:12px;
    ">
        CRIMSON NOVA TECHNOLOGY
    </p>

</div>
""")

st.sidebar.markdown("---")


# ==========================================
# 8. AI SETTINGS
# ==========================================

st.sidebar.markdown("### ⚙️ AI SETTINGS")

st.sidebar.selectbox(
    "Select Local Model",
    ["Gemma 3:1B"],
    disabled=True
)


# ==========================================
# 9. MEMORY INFORMATION
# ==========================================

st.sidebar.html("""
<div class="memory-card">

    <h4 style="color:#FF5555;">
        🧠 Memory System
    </h4>

    <p style="color:white;">
        LangChain Conversation Memory
    </p>

    <p style="color:white;">
        Remembers previous messages.
    </p>

</div>
""")


st.sidebar.markdown("---")


# ==========================================
# 10. CHAT HISTORY
# ==========================================

st.sidebar.markdown("### 📚 CHAT HISTORY")

st.sidebar.metric(
    "Total Messages",
    len(st.session_state.messages)
)

st.sidebar.caption("Current conversation")


# ==========================================
# 11. CLEAR CURRENT CHAT
# ==========================================

if st.sidebar.button(
    "🗑️ Clear Current Chat",
    use_container_width=True
):

    st.session_state.messages = []

    if SESSION_ID in st.session_state.history_store:
        st.session_state.history_store[SESSION_ID].clear()

    st.rerun()


# ==========================================
# 12. CLEAR ALL MEMORY
# ==========================================

if st.sidebar.button(
    "♻️ Clear All Memory",
    use_container_width=True
):

    st.session_state.messages = []
    st.session_state.history_store = {}

    st.rerun()


# ==========================================
# 13. MAIN HEADER
# ==========================================

st.html("""
<div class="main-header">

    <div class="ai-logo">✦</div>

    <div class="main-title">
        SYNORA AI
    </div>

    <div class="subtitle">
        Smart Conversations. Intelligent Memory.
    </div>

    <p style="
        color:#4ADE80;
        font-weight:bold;
        margin-top:15px;
    ">
        ● LOCAL AI ASSISTANT
    </p>

</div>
""")


# ==========================================
# 14. INITIALIZE MODEL
# ==========================================

try:

    llm = load_llm()
    chatbot = create_chatbot(llm)

except Exception as error:

    st.error(f"Model initialization failed: {error}")

    st.info(
        "Check whether Ollama is running "
        "and Gemma 3:1B is installed."
    )

    st.stop()


# ==========================================
# 15. DISPLAY OLD MESSAGES
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"],
        avatar="🧑" if message["role"] == "user" else "🤖"
    ):

        st.markdown(message["content"])


# ==========================================
# 16. CHAT INPUT
# ==========================================

user_input = st.chat_input(
    "Ask SYNORA anything..."
)


if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)

    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("SYNORA is thinking..."):

            try:

                response = chatbot.invoke(

                    {"input": user_input},

                    config={
                        "configurable": {
                            "session_id": SESSION_ID
                        }
                    }
                )

                answer = response.content

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as error:

                st.error(f"Error: {error}")

                st.info(
                    "Make sure Ollama is running "
                    "and Gemma 3:1B is installed."
                )

                st.session_state.messages.pop()


# ==========================================
# 17. VIEW CONVERSATION MEMORY
# ==========================================

st.markdown("---")

with st.expander("🧠 VIEW CONVERSATION MEMORY"):

    memory = get_session_history(SESSION_ID)

    if memory.messages:

        for msg in memory.messages:

            role = (
                "You"
                if msg.type == "human"
                else "SYNORA AI"
            )

            st.markdown(f"**{role}:** {msg.content}")

    else:

        st.info("No conversation memory available yet.")


# ==========================================
# 18. FOOTER
# ==========================================

st.html("""
<div class="footer">

    <p>Powered by Gemma 3:1B</p>

    <p>Built with LangChain Memory</p>

    <p>SYNORA AI © 2026</p>

</div>
""")
