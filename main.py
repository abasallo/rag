import os

from dotenv import load_dotenv, find_dotenv

from langchain.embeddings import OpenAIEmbeddings

from vector_db.chroma_database import ChromaDatabase
from vector_db.chroma_document import ChromaDocument

from llm.open_ai import OpenAI

from load_json_file import load_json_file

JSON_FILE_PATH = "data.json"

VECTOR_DATABASE_NAME = "my_database"

load_dotenv(find_dotenv())
OPENAI_EMBEDDING_MODEL = os.getenv('OPENAI_EMBEDDING_MODEL')
OPENAI_CHAT_MODEL = os.getenv('OPENAI_CHAT_MODEL')


def main():
    json = load_json_file(JSON_FILE_PATH)

    db = ChromaDatabase(db_name=VECTOR_DATABASE_NAME,
                        embeddings=OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL),
                        documents=ChromaDocument.extract_fields(json))

    open_ai = OpenAI(model=OPENAI_CHAT_MODEL)

    query = input("\nRAG query for the LLM?:\n\n")

    similar_docs = db.find_similar_docs(query, 2)
    ChromaDatabase.log(similar_docs)

    answer = open_ai.rag_query(query, similar_docs)
    OpenAI.log(answer)


if __name__ == "__main__":
    main()
