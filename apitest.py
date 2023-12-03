import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel


from article_processing import modules, modules_without_functions


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

@app.get("/api/modules")
async def get_modules():
    return modules_without_functions


@app.post("/api/modules/{module_name}")
async def run_module(module_name: str, article: Article):
    if module_name in modules:
        return {
            "module_name": module_name,
            "result": modules.get(module_name).get("function")(article.text)
        }
    else:
        raise HTTPException(status_code=404)

@app.post("/api/module/question_answering")
async def question_answering(text: str, question: str = "") -> str:
    from ArticleProcessing.article_processing.question_answering import qa_model
    answer = qa_model(question=question, context=text)
    return answer["answer"]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)