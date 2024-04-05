from keywords import Keywords
from info_retriever import Info_Retriever
from info_ranker import Info_Ranker
from answr_DistilBert import DistilBertAnswerGenerator
from answr_RoBERTa import RoBERTaAnswerGenerator
from fastapi import FastAPI


import logging
logging.basicConfig(level=logging.INFO, 
                    filename="log.log", 
                    filemode="w",
                    format="%(asctime)s - %(levelname)s -%(message)s")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Q&A API!"}

# user input
query = input("Any question? ")

# keyword extraction from user input
kw = Keywords()
keywords = kw.extract_keywords(query)

# info retrieving ('n' most relevant documents based on BM25)
n = 5
collector = Info_Retriever()
document_list, pages_list = collector.get_info(keywords)

ranker = Info_Ranker(document_list)
top_documents = ranker.rank_documents(document_list, query, n)


# LLM: questions + answers
DistilBert_answer_generator = DistilBertAnswerGenerator(top_documents,query)
# # RoBERTa_answer_generator = RoBERTaAnswerGenerator()
logging.info(' Answers are:')

answers_list = []
for i in range(len(top_documents)):

    answer = DistilBert_answer_generator.generate_answer(top_documents[i],query)
    # answer = RoBERTa_answer_generator.generate_answer(top_documents[i], query)
    answers_list.append(answer)

    print('Answer {}: {}'.format(i, answer))
    logging.info(f' {i}{answer}')
