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

@app.get("/answers")
def Question_Answer(query: str):
    try:
        kw = Keywords()
        keywords = kw.extract_keywords(query)

        collector = Info_Retriever()
        document_list, pages_list = collector.get_info(keywords)

        ranker = Info_Ranker(document_list)
        top_documents = ranker.rank_documents(document_list, query, 10)
        
        DistilBert_answer_generator = DistilBertAnswerGenerator(top_documents,query)
        answers_list = []
        for i in range(len(top_documents)):
            answer = DistilBert_answer_generator.generate_answer(top_documents[i],query)
            
            # non_empty_positions:
            if answer.strip():
                logging.info(f' Answer {i}: {answer}')
                answers_list.append(answer)
        
        return answers_list

    except Exception as e:
        logging.error(e)
        return {"error": str(e)}


#############################################
### WITHOUT API CONNECTION (PREVIOUS STEP)###
#############################################
## 1. user input
# query = input("Any question? ")

## 2. keyword extraction from user input
# kw = Keywords()
# keywords = kw.extract_keywords(query)

## 3. info retrieving ('n' most relevant documents based on BM25)
# n = 5
# collector = Info_Retriever()
# document_list, pages_list = collector.get_info(keywords)

# ranker = Info_Ranker(document_list)
# top_documents = ranker.rank_documents(document_list, query, n)

## 4. LLM: questions + answers
# DistilBert_answer_generator = DistilBertAnswerGenerator(top_documents,query)
# # # RoBERTa_answer_generator = RoBERTaAnswerGenerator()
# logging.info(' Answers are:')

# answers_list = []
# for i in range(len(top_documents)):
#     answer = DistilBert_answer_generator.generate_answer(top_documents[i],query)
#     # answer = RoBERTa_answer_generator.generate_answer(top_documents[i], query)
#     answers_list.append(answer)

# 5. ouput representation
#     print('Answer {}: {}'.format(i, answer))
#     logging.info(f' {i}{answer}')

#############################################
#############################################