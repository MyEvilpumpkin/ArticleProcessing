from transformers import BertTokenizer, BertForSequenceClassification
import torch
import numpy as np
import json

model_name = 'Skoltech/russian-sensitive-topics'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

with open("article_processing/sensitive_topics_ids.json") as f:
    sensitive_topics_ids = json.load(f)


def execute(text: str) -> str:
    tokenized = tokenizer.batch_encode_plus(
        [text],
        max_length=512,
        pad_to_max_length=True,
        truncation=True,
        return_token_type_ids=False)

    tokens_ids = torch.tensor(tokenized['input_ids'])
    mask = torch.tensor(tokenized['attention_mask'])

    with torch.no_grad():
        model_output = model(tokens_ids, mask)

    topic_scores = model_output['logits'][0]
    topic_index = str(int(np.argmax(topic_scores)))
    topic = sensitive_topics_ids[topic_index]
    return topic
