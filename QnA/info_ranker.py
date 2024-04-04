from rank_bm25 import BM25Okapi
import logging

class Info_Ranker():
    def __init__(self, documents):
        self.tokenized_corpus = [doc.split(' ') for doc in documents]
        self.bm25 = BM25Okapi(self.tokenized_corpus)

    def rank_documents(self, documents, query, n):
        try:
            # tokenized_corpus = [doc.split(' ') for doc in documents]
            tokenized_query = query.split(" ")
            doc_scores = self.bm25.get_scores(tokenized_query)
            top_documents = self.bm25.get_top_n(tokenized_query, documents, n)
            
            logging.info(f' Most Relevant Documents: ')
            for doc in top_documents:
                logging.info(f' - {doc} ...')

            return top_documents
        
        except Exception as e:
            print("Error:", e)
            return []
    