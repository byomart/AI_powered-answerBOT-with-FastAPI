from transformers import RobertaTokenizer, RobertaForQuestionAnswering
import torch

class RoBERTaAnswerGenerator:
    def __init__(self):
        self.tokenizer = RobertaTokenizer.from_pretrained('roberta-base', return_token_type_ids=True)
        self.model = RobertaForQuestionAnswering.from_pretrained('roberta-base', return_dict=False)

    def generate_answer(self, context, question):
        encoding = self.tokenizer.encode_plus(question, context, return_tensors='pt')
        input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]
        start_scores, end_scores = self.model(input_ids, attention_mask=attention_mask)
        start_index = torch.argmax(start_scores)
        end_index = torch.argmax(end_scores)
        answer_tokens = input_ids[0][start_index : end_index+1]
        start_index = torch.argmax(start_scores)
        end_index = torch.argmax(end_scores)
        answer_tokens = input_ids[0][start_index : end_index+1]
        answer = self.tokenizer.decode(answer_tokens.tolist()) 
        
        return answer
