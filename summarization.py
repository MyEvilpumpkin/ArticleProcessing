import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

article_text = """
    С 1 октября российский Центробанк начал по-новому рассекречивать мошенников, напомнил резидент Экспертного клуба ЦСР Глеб Белавин. Теперь банки начали передавать регулятору данные о переводах, которые кажутся сомнительными.

До этого ЦБ получал только сведения о конечном получателе похищенных средств. Теперь банки будут раскрывать информацию о подозрительных транзакциях по 50 признакам. Среди прочего, речь идет о большем количестве данных о переводах, сделанных без согласия владельца счета. Как говорил экономический обозреватель Вячеслав Абрамов, нововведение может принести некоторые дополнительные неудобства для бизнеса, но серьезных ухудшений не будет.

Ранее депутат Госдумы Денис Кравченко в разговоре с «Лентой.ру» заявил, что возможности мошенников уже существенно ограничены, что в значительной степени повышает уровень защиты граждан. Тем не менее работа по совершенствованию безопасности персональных данных россиян продолжается.
"""

model_name = "csebuetnlp/mT5_multilingual_XLSum"
tokenizer = AutoTokenizer.from_pretrained(model_name, legacy=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

input_ids = tokenizer(
    [WHITESPACE_HANDLER(article_text)],
    return_tensors="pt",
    padding="max_length",
    truncation=True,
    max_length=512
)["input_ids"]

output_ids = model.generate(
    input_ids=input_ids,
    max_length=84,
    no_repeat_ngram_size=2,
    num_beams=4
)[0]

summary = tokenizer.decode(
    output_ids,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)

print(summary)
