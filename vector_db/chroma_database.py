from typing import List, Type

from langchain.vectorstores import Chroma as ChromaVectorStore

from vector_db.chroma_document import ChromaDocument


class ChromaDatabase:

    def __init__(self, db_name, embeddings, documents: List[Type['ChromaDocument']]):
        self.db_name = db_name
        self.db = ChromaDatabase._load(db_name, embeddings, documents)

    @staticmethod
    def _load(db_name, embeddings, documents):
        chroma_vector_store = ChromaVectorStore(db_name)
        db = chroma_vector_store.from_documents(documents, embeddings)
        return db

    def find_similar_docs(self, query, k, score=None):
        if score:
            return self.db.similarity_search_with_score(query, k)
        else:
            return self.db.similarity_search(query, k)

    @staticmethod
    def log(docs: List[ChromaDocument]):
        print("\nLocal Database Contents:")
        print(f"\nNumber of Documents: {len(docs)}")
        index = 1
        for doc in docs:
            print(f"\n{index} - {doc.page_content}")
            index += 1
