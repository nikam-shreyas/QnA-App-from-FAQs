import os
from dotenv import load_dotenv

from langchain.llms import GooglePalm
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

load_dotenv()

CSV_FILE_PATH = "codebasics_faqs.csv"

instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")

VECTOR_DB_FILE_PATH = "vector_db"

llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=1)


def create_vector_db():
    loader = CSVLoader(file_path=CSV_FILE_PATH, source_column="prompt", encoding='cp1252')
    data = loader.load()
    vectordb = FAISS.from_documents(documents = data, embedding=instructor_embeddings)
    vectordb.save_local(VECTOR_DB_FILE_PATH)


def load_vector_db():
    try:
        vectordb = FAISS.load_local(VECTOR_DB_FILE_PATH, instructor_embeddings)
    except RuntimeError as e:
        print("Creating vector database. This step may take some time.")
        create_vector_db()
        print("Vector Database created.")
        vectordb = FAISS.load_local(VECTOR_DB_FILE_PATH, instructor_embeddings)
    return vectordb

def get_chain():
    vector_db = load_vector_db()
    retirever = vector_db.as_retriever()
    prompt = PromptTemplate(template="""Answer the question based on the context provided below. If the answer is not present in the context, say "I don't know". 
    Context: {context}
    Question: {question}
    """, input_variables = ["context", "question"])

    
    chain = RetrievalQA.from_chain_type(llm=llm, 
                                        retriever=retirever, 
                                        chain_type="stuff", 
                                        input_key="query", 
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt":prompt})

    return chain


