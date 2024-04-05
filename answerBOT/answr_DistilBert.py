from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
import torch
import logging

class DistilBertAnswerGenerator:
    def __init__(self, context, question):
        self.tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased', return_token_type_ids=True)
        self.model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad', return_dict=False)
        self.context = context
        self.question = question

    def generate_answer(self, doc, query):
        encoding = self.tokenizer.encode_plus(query, doc)
        input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]
        start_scores, end_scores = self.model(torch.tensor([input_ids]), attention_mask=torch.tensor([attention_mask]))
        ans_tokens = input_ids[torch.argmax(start_scores): torch.argmax(end_scores) + 1]
        answer_tokens = self.tokenizer.convert_ids_to_tokens(ans_tokens, skip_special_tokens=True)
        answer = self.tokenizer.convert_tokens_to_string(answer_tokens)

        # if answer.strip():
        #     logging.info(f'{answer}')

        return answer
