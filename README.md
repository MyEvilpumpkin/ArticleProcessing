# ArticleProcessing

Application for processing news (and other) articles

## Used models
Module | Model | Included in the app | Unit tests written | Contributor
-|-|-|-|-
Genre Definition | MoritzLaurer/mDeBERTa-v3-base-mnli-xnli | ✔️ | ✔️ | Dmitriy Tomin
Summarization | d0rj/rut5-base-summ | ✔️ | | Dmitriy Tomin
Language detection | papluca/xlm-roberta-base-language-detection | | ✔️ | Artem Oleynik
## Web apps

### Streamlit

#### D.Tomin
[![](https://docs.streamlit.io/logo.svg)App file](streamlit_app.py)  
[![](https://docs.streamlit.io/logo.svg)Demo app](https://articleprocessing.streamlit.app) (some features are disabled)

https://github.com/MyEvilpumpkin/ArticleProcessing/assets/24656713/ad4bf0ce-3e95-48a9-8f3d-ee4f62aa7f83

#### A.Oleynik
**Model:** [papluca/xlm-roberta-base-language-detection](https://huggingface.co/papluca/xlm-roberta-base-language-detection)  
**Run local:** streamlit run streamlit_app.py  
**Details:** Type the required text in the input field and press Ctrl+Enter.  
The expected language of the entered text will appear below the input field.

![View of the working application](https://github.com/MyEvilpumpkin/ArticleProcessing/assets/13471304/8a4bfc0b-d6c1-48ce-977c-c26417b18556)

### FastAPI

[![](!https://fastapi.tiangolo.com/ru/img/icon-white.svg)App file](web_app.py)

https://github.com/MyEvilpumpkin/ArticleProcessing/assets/24656713/6d9f6047-a72e-43bd-9fbc-77e6a4733d2e

https://github.com/MyEvilpumpkin/ArticleProcessing/assets/24656713/3241c7f4-acd2-4169-a604-2fc10c736158

https://github.com/MyEvilpumpkin/ArticleProcessing/assets/24656713/dd59326c-a48b-47ca-a9ad-7effe988213f

