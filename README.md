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

`git clone https://github.com/MyEvilpumpkin/ArticleProcessing.git`

2. Install the dependencies:

`pip install -r requirements.txt`

### Option 2: Use Docker

1. Clone the repository:

`git clone https://github.com/MyEvilpumpkin/ArticleProcessing.git`

2. Build the Docker image:

`docker compose build article_processing`

## Usage

To run the Streamlit app:

`streamlit run streamlit_app.py`

To run the FastAPI app:

`uvicorn web_app:app --reload`

To run the Docker container:

`docker compose up -d article_processing_streamlit`

## API Endpoints

While using FastAPI option, application provides the following API endpoints:

- `GET /api/modules`: Returns a list of all available modules. No request body is needed. The response is a JSON object where the keys are the module names and the values are objects containing information about each module.

- `POST /api/modules/{module_name}`: Runs a specific module with the provided article text. The request body should be a JSON object with a single key, "text", containing the article text as a string. The `module_name` in the URL should be replaced with the name of the module you want to run. The response is a JSON object containing the module name and the result of running the module on the provided text.

You can access interactive documentation for these endpoints by running the application and navigating to `/docs` on the application's base URL (e.g., `http://localhost:8000/docs` for a locally running application).

## DVC Storage

[Google Drive](https://drive.google.com/drive/folders/1Az-aH4Vnxvo1D7pdFVPiJ6Sb1o7UDj6X)
