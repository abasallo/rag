import os

from dotenv import load_dotenv, find_dotenv

from langchain.adapters import openai
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI

load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_CHAT_TEMPERATURE = os.getenv('OPENAI_CHAT_TEMPERATURE')


class OpenAI:

    openai.api_key = OPENAI_API_KEY

    def __init__(self, model):
        self.model = model

    @staticmethod
    def _get_answer(query, chain, similar_docs):
        answer = chain.run(input_documents=similar_docs, question=query)
        return answer

    def rag_query(self, query, similar_docs):
        llm = ChatOpenAI(model_name=self.model, temperature=OPENAI_CHAT_TEMPERATURE)
        chain = load_qa_chain(llm, chain_type="stuff")
        answer = OpenAI._get_answer(query, chain, similar_docs)
        return answer

    @staticmethod
    def log(answer):
        print(f"\nLLM Answer:\n\n{answer}")
