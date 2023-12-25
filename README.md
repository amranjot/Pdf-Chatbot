# LLM Chat App

## Overview
This project is a Chatbot application powered by LangChain and OpenAI's LLM (Language Model) built using Streamlit. The app allows users to interact with a PDF file by uploading it and asking questions related to the content. The text in the PDF is processed using LangChain to generate embeddings, and OpenAI's LLM is used for question-answering.

## Technologies Used
- [Streamlit](https://streamlit.io/): A Python library for creating web applications with minimal code.
- [LangChain](https://github.com/LangChain/langchain): A library for natural language processing and understanding.
- [OpenAI](https://openai.com/): The organization providing powerful language models like GPT-3.5-turbo.
- [PyPDF2](https://pythonhosted.org/PyPDF2/): A Python library for reading PDF files.
- [FAISS](https://github.com/facebookresearch/faiss): Facebook AI Similarity Search, used for vector similarity search.
- [dotenv](https://github.com/theskumar/python-dotenv): A Python library for reading variables from `.env` files.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/llm-chat-app.git
    cd llm-chat-app
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables by creating a `.env` file and adding the necessary information.

## Usage
Run the application using the following command:
```bash
streamlit run app.py


