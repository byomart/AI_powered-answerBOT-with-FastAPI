from keywords import Keywords
from info_retriever import Info_Retriever
from info_ranker import Info_Ranker
from answr_DistilBert import DistilBertAnswerGenerator
from answr_RoBERTa import RoBERTaAnswerGenerator



import logging
logging.basicConfig(level=logging.INFO, 
                    filename="log.log", 
                    filemode="w",
                    format="%(asctime)s - %(levelname)s -%(message)s")


# user input
query = input("Any question? ")

# keyword extraction from user input
kw = Keywords()
keywords = kw.extract_keywords(query)

# info retrieving ('n' most relevant documents based on BM25)
n = 5
collector = Info_Retriever()
document_list, pages_list = collector.get_info(keywords)

ranker = Info_Ranker()
top_documents = ranker.rank_documents(document_list, query, n)


# # LLM: questions + answers
DistilBert_answer_generator = DistilBertAnswerGenerator()
# # RoBERTa_answer_generator = RoBERTaAnswerGenerator()

answers_list = []
for i in range(len(top_documents)):
    answer = DistilBert_answer_generator.generate_answer(top_documents[i], query)
    answers_list.append(answer)

for i, answer in enumerate(answers_list, 1):
    print(f"Respuesta {i}: {answer}")