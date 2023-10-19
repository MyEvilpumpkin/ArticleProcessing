import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from article_processing import functions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Article(BaseModel):
    text: str


@app.post("/api/{function_name}")
async def execute_function(function_name: str, article: Article):
    if function_name in functions:
        return {
            "function_name": function_name,
            "result": functions.get(function_name)(article.text)
        }
    else:
        raise HTTPException(status_code=404)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

