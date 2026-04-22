 MedRAG – Healthcare Chatbot (RAG-based)

MedRAG is a lightweight Retrieval-Augmented Generation (RAG) chatbot designed to answer healthcare-related queries using a local medical knowledge base. It uses FAISS vector search and a custom embedding approach to retrieve relevant information and generate responses.

 Features
🔍 Retrieval-based chatbot using FAISS
🧠 Custom lightweight embeddings (no heavy ML models required)
🏥 Healthcare-focused responses
⚠️ Built-in medical safety guardrails
💬 Interactive UI using Streamlit
⚡ Fast and local execution


Tech Stack
Language: Python
Libraries:
langchain
faiss
streamlit


Concepts Used:
RAG (Retrieval-Augmented Generation)
Vector Search
Text Chunking


📂 Project Structure
medrag/
│── ingest.py            # Converts raw data into vector embeddings
│── rag_pipeline.py      # Core chatbot logic (retrieval + response)
│── web.py               # Streamlit UI
│── sample_data.txt      # Medical knowledge base
│── vectorstore/         # Stored FAISS index
│── README.md            # Documentation


How It Works

1️⃣ Data Ingestion (ingest.py)
Reads medical text data
Splits into smaller chunks
Converts text → embeddings
Stores embeddings in FAISS vector database

2️⃣ Retrieval + Response (rag_pipeline.py)
Converts user query → embedding
Retrieves top relevant documents
Returns context-based answer
Adds safety disclaimer

3️⃣ User Interface (web.py)
Built using Streamlit
Accepts user queries
Displays chatbot responses


 Installation & Setup
 
1️⃣ Clone the Repository
git clone https://github.com/joseanifer-b/chatbot.git
cd chatbot

2️⃣ Create Virtual Environment
python3 -m venv myenv
source myenv/bin/activate

3️⃣ Install Dependencies
pip install streamlit langchain faiss-cpu

4️⃣ Add Dataset
Create a file:
sample_data.txt
Add medical information (e.g., diseases, symptoms, treatments).

5️⃣ Run Data Ingestion
python ingest.py
 This creates the vectorstore/ folder

6️⃣ Run the Chatbot
streamlit run web.py
  Example Usage
User: What is diabetes?
Bot: Based on the medical information database:
Diabetes is a chronic condition...
  This information is for educational purposes only...
  Safety Features
Detects sensitive keywords:
suicide
self harm
overdose
Returns emergency warning instead of unsafe response

 Limitations
Uses simple hash-based embeddings (not semantic)
Limited understanding compared to LLMs
Depends on quality of sample_data.txt

Future Improvements
 Replace custom embeddings with transformer models
 Add API-based LLM (OpenAI / Gemini)
 Improve semantic understanding
 Add voice interaction
 Store chat history in database
 
 Use Cases
Healthcare FAQ assistant
Educational chatbot
Prototype for medical AI systems


