import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import pickle
from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback

# Sidebar contents
with st.sidebar:
    st.title(" LLM Chat App")
    st.markdown('''
                ## About
                This app is an LLM-powered Chatbot built using:
                - [Streamlit]
                - [LangChain]
                - [OpenAI] LLM Model
                ''')
    add_vertical_space(5)
    st.write("Made By Ranjot")



def main():
    st.header("Chat with any Pdf 💬")
    
    load_dotenv()
    
    # upload a PDF File
    pdf = st.file_uploader("Upload your PDF",type='pdf')
    
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        
        # Extract Text form the Pdf File.
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
            
        
        # By using Langchain text splitter we can split text into chuncks.
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len
        )
        
        chunks = text_splitter.split_text(text=text)
            
        # Embeddings
        
        store_name = pdf.name[:-4]
        
        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl",'rb') as f:
                VectorStore = pickle.load(f)
            st.write("Embeddings Loading From Disk")
        
        else :
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks,embedding=embeddings) 
            with open(f"{store_name}.pkl",'wb') as f:
                pickle.dump(VectorStore,f)
                
            st.write("Embeddings Computation Completed")
            
            
        # Accept user questions/query
        query  = st.text_input("Ask questions about your PDF File")
        st.write(query)
        
        if query:
            docs = VectorStore.similarity_search(query=query,k=3)
            llm = OpenAI(model_name='gpt-3.5-turbo')
            chain = load_qa_chain(llm=llm,chain_type='stuff')
            
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query)
                print(cb)
            
            st.write(response) 
   
    
    


if __name__ == "__main__":
    main()