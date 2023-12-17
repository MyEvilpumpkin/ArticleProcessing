# ArticleProcessing

ArticleProcessing is a Python application that uses advanced natural language processing techniques to analyze news articles. The application can determine the genre of a text, analyze its sentiment, detect the language, translate the text, and summarize the text. 

The application uses various models from the Hugging Face Transformers library for these tasks, and also provides a user interface built with Streamlit and FastAPI. It can be deployed as a Docker container, making it easy to set up and run on any system.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **Genre Definition**: Determines the genre of a given text. Uses the "MoritzLaurer/mDeBERTa-v3-base-mnli-xnli" model for zero-shot classification.
- **Sentiment Analysis**: Analyzes the sentiment of a given text. Uses the "blanchefort/rubert-base-cased-sentiment" model.
- **Language Detection**: Detects the language of a given text. Uses the "papluca/xlm-roberta-base-language-detection" model.
- **Translation**: Translates a given text from one language to another. Uses the "Helsinki-NLP/opus-mt-ru-en" model.
- **Summarization**: Summarizes a given text. Uses the "d0rj/rut5-base-summ" model.


## Installation

You can set up and run ArticleProcessing in two ways: by installing the dependencies and running it directly on your machine, or by building a Docker image and running it as a Docker container.

### Option 1: Install dependencies

1. Clone the repository:

`git clone https://github.com/MyEvilpumpkin/ArticleProcessing.git`.

2. Install the dependencies:

`bash pip install -r requirements.txt`

### Option 2: Use Docker

1. Clone the repository:

`git clone https://github.com/MyEvilpumpkin/ArticleProcessing.git`.

2. Build the Docker image:

`bash docker build -t articleprocessing .`

## Usage

To run the Streamlit app:

`bash streamlit run streamlit_app.py`

To run the FastAPI app:

`bash uvicorn web_app:app --reload`

To run the Docker container:

`bash docker run -p 8501:8501`