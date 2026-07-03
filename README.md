# AI-Powered Retrieval-Augmented Generation Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that allows users to query their own documents using natural language. The system automatically loads documents, generates embeddings using SentenceTransformers, performs semantic search using FAISS, and generates context-aware responses using Groq-hosted Large Language Models.

The project provides a simple Streamlit-based chat interface for interacting with local document collections.
Live: https://a-complete-rag-software-3ockwxfgcfp5uwgs3yjevp.streamlit.app/

## Features

### Document Loading

* Supports multiple document formats:

  * PDF
  * TXT
  * CSV
  * Excel (.xlsx)
  * Word (.docx)
  * JSON
* Recursive folder scanning
* Metadata preservation

### Intelligent Chunking

* RecursiveCharacterTextSplitter
* Configurable chunk size 
* Context-preserving document segmentation

### Embedding Generation

* SentenceTransformers integration
* Default embedding model:

  * all-MiniLM-L6-v2
* Fast semantic vector generation

### Vector Search

* FAISS vector database
* Persistent storage of embeddings
* Fast similarity search


### AI-Powered Question Answering

* Groq LLM integration
* Context-aware answer generation
* Retrieval-Augmented Generation workflow

### Interactive Chat Interface

* Streamlit chatbot UI
* ChatGPT-style interaction
* Real-time document querying





## Tech Stack

### AI & Machine Learning

* LangChain
* SentenceTransformers
* FAISS
* Groq LLM

### Frontend

* Streamlit

## Setup

```bash
# Clone repository
git clone https://github.com/hasnatsamiul/A-complete-RAG-Software.git

# Enter project directory
cd A-complete-RAG-Software

# Create virtual environment
uv venv

# Activate environment
source .venv/bin/activate

# Install dependencies
uv add -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can generate a Groq API key from:

https://console.groq.com/keys

## Build the Vector Database

Place your documents inside the `data/` directory and run:

```bash
python app.py
```

The application will:

1. Load all documents
2. Split documents into chunks
3. Generate embeddings
4. Build the FAISS vector database
5. Save the index locally

## Run the Chatbot

```bash
python -m streamlit run frontend.py
```

Open:

```text
http://localhost:8501
```

## Example Questions

```text
What is ForecastTKGQuestions?

What are the applications of Temporal Knowledge Graphs (TKGs)?

What are the main findings of the uploaded documents?

Provide a summary of the uploaded PDFs.
```
<img width="1503" height="805" alt="Screenshot 2026-06-25 at 12 12 47" src="https://github.com/user-attachments/assets/ceee4b91-35db-4763-943e-459e0ba1a9e8" />


## Supported Embedding Models

* all-MiniLM-L6-v2

## Supported Groq Models

* llama-3.3-70b-versatile
* llama-3.1-8b-instant

## Future Improvements

* Conversational memory
* Source citations
* ChromaDB support
* Document upload through UI
* Docker deployment
* Multi-user authentication

## Author

**S M Hasnat Samiul**

M.Sc. High Integrity Systems
Frankfurt University of Applied Sciences,
email: smhasnats@gmail.com

## License

MIT License

This project is open-source and available for educational and research purposes.
