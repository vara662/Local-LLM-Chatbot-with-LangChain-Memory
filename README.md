# SYNORA AI – Local LLM Chatbot with LangChain Memory

**SYNORA AI** is a futuristic AI chatbot built using Streamlit, LangChain, and Ollama. It uses the locally running **Gemma 3:1B** language model to provide intelligent conversations while remembering previous messages using LangChain Conversation Memory.

## Project Overview

SYNORA AI is a personal AI assistant designed to demonstrate how Large Language Models (LLMs) can be integrated with conversational memory.

Unlike a basic chatbot, SYNORA AI can remember previous messages and use conversation history to provide context-aware responses.

## Features

- Local AI chatbot powered by Gemma 3:1B.
- LangChain conversation memory.
- Interactive chat interface.
- Conversation history.
- Clear current chat option.
- Clear all memory option.
- View conversation memory.
- Futuristic crimson-red user interface.
- Local model execution using Ollama.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Streamlit | User interface |
| Ollama | Run local LLM |
| Gemma 3:1B | Language model |
| LangChain | LLM integration |
| LangChain Memory | Conversation history |

## Project Structure

```text
SYNORA-AI/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project

```bash
cd SYNORA-AI
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Install Ollama

Download Ollama from:

https://ollama.com/

### Step 5: Download the Gemma Model

```bash
ollama pull gemma3:1b
```

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## How LangChain Memory Works

SYNORA AI uses LangChain's `RunnableWithMessageHistory` and `InMemoryChatMessageHistory`.

1. The user enters a message.
2. LangChain retrieves the previous conversation.
3. The conversation history is passed to the LLM.
4. Gemma 3:1B generates a response.
5. The user message and AI response are stored in conversation memory.
6. The chatbot uses stored messages in future responses.

**Note:** Conversation memory is maintained during the active application session. It is not permanently stored after restarting the application.

## Example Conversation

**User:** My name is Arun.

**SYNORA AI:** Nice to meet you, Arun!

**User:** What is my name?

**SYNORA AI:** Your name is Arun.

This demonstrates the chatbot's ability to remember previous conversations.

## Future Enhancements

- Permanent conversation storage.
- Multiple chat sessions.
- User authentication.
- Voice input and output.
- File upload and document analysis.
- Improved AI response generation.

## Project Information

**Project Name:** SYNORA AI

**Project Type:** LLM Chatbot

**Model:** Gemma 3:1B

**Framework:** Streamlit and LangChain

**Execution:** Local using Ollama

## License

This project is created for educational and learning purposes.

---

**SYNORA AI – Smart Conversations. Intelligent Memory.**
