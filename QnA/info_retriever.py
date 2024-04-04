import wikipedia
import logging 


class Info_Retriever:
    def __init__(self):
        pass

    def get_info(self, keywords):

        wiki_pages = wikipedia.search(keywords, results=10)
        logging.info(f' Wikipedia Pages: {wiki_pages}')

        document_list = []
        pages_list = []
        for page in wiki_pages:
            try:
                info_summary = wikipedia.summary(page)
                if any(word in info_summary.lower() for word in keywords):
                    document_list.append(info_summary)
                    pages_list.append(page)
            except:
                pass

        # limiting the len 
        document_list = [item[:1000] for item in document_list] 
        
        logging.info(f' Trimmed Wikipedia Entries: {document_list}')
        logging.info(f' Final Wikipedia Pages: {pages_list}')
        
        return document_list, pages_list

