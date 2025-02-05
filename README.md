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
git clone https://github.com/gduartels/bbc-qna-chatbot-poc.git
cd project-directory

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```
### Configuration

1. Create `secrets.toml` in `.streamlit/` directory:
```toml
OPENAI_API_KEY = "your-api-key-here"
```
2. Add documents to `md_files/` directory

## 🛠 Usage

### Generate Embeddings
```bash
python embeddings.py
```

### Run Application
```bash
streamlit run app.py
```

## 📁 Project Structure
```bash
├── md_files/              # Document storage
├── Embedding/             # Vector database
├── .streamlit/
│   └── secrets.toml      # API credentials
├── embeddings.py         # Vector DB creation
├── model.py              # LLM & chain configuration
├── app.py                # Streamlit interface
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```
