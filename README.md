# BBC Digital Chatbot with RAG

A Retrieval-Augmented Generation (RAG) chatbot prototype that answers questions about company information using custom documentation.

![Chatbot Interface](image.png)

## 📖 Project Overview
This chatbot leverages LangChain and ChromaDB to provide context-aware answers based on company documentation stored in markdown and PDF files. The solution features:
- Streamlit web interface for user interaction
- Local vector storage with ChromaDB
- Conversation history management
- GPT-4 powered responses

## ✨ Key Features
- **RAG Implementation**: Combines retrieval from documents with generative AI
- **Conversational Memory**: Maintains context-aware dialogues
- **Local Vector Store**: ChromaDB for efficient document retrieval
- **Multi-File Support**: Processes both markdown and PDF documents
- **Session Management**: Supports multiple concurrent conversations

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- OpenAI API key
- Streamlit account

### Installation
```bash
# Clone repository
git clone [your-repository-url]
cd project-directory

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```
