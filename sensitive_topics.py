from transformers import BertTokenizer, BertForSequenceClassification
import torch
import numpy as np

model_name = 'Skoltech/russian-sensitive-topics'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

import json
with open("id2topic.json") as f:
    target_vaiables_id2topic_dict = json.load(f)

article_text = """
    С 1 октября российский Центробанк начал по-новому рассекречивать мошенников, напомнил резидент Экспертного клуба ЦСР Глеб Белавин. Теперь банки начали передавать регулятору данные о переводах, которые кажутся сомнительными.

До этого ЦБ получал только сведения о конечном получателе похищенных средств. Теперь банки будут раскрывать информацию о подозрительных транзакциях по 50 признакам. Среди прочего, речь идет о большем количестве данных о переводах, сделанных без согласия владельца счета. Как говорил экономический обозреватель Вячеслав Абрамов, нововведение может принести некоторые дополнительные неудобства для бизнеса, но серьезных ухудшений не будет.

Ранее депутат Госдумы Денис Кравченко в разговоре с «Лентой.ру» заявил, что возможности мошенников уже существенно ограничены, что в значительной степени повышает уровень защиты граждан. Тем не менее работа по совершенствованию безопасности персональных данных россиян продолжается.
"""

article_summarization = """Российские банки будут передавать регулятору данные о подозрительных транзакциях, сообщили в Центробанке России."""

tokenized = tokenizer.batch_encode_plus([article_text],
    max_length = 512,
    pad_to_max_length=True,
    truncation=True,
    return_token_type_ids=False)
tokens_ids,mask = torch.tensor(tokenized['input_ids']),torch.tensor(tokenized['attention_mask'])



with torch.no_grad():
    model_output = model(tokens_ids,mask)

def adjust_multilabel(y, is_pred = False):
    y_adjusted = []
    for y_c in y:
        y_test_curr = [0]*19
        index = str(int(np.argmax(y_c)))
        y_c = target_vaiables_id2topic_dict[index]
    return y_c

preds = adjust_multilabel(model_output['logits'], is_pred = True)
print(preds)
