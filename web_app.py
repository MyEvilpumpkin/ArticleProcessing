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


@app.get("/api/modules", summary="Get Modules", description="Returns a list of all available modules.")
async def get_modules():
    return modules_without_functions

@app.post("/api/modules/{module_name}", summary="Run Module", description="Runs a specific module with the provided article text.")
async def run_module(module_name: str, article: Article):
    if module_name in modules:
        return {
            "module_name": module_name,
            "result": modules.get(module_name).get("function")(article.text)
        }
    else:
        raise HTTPException(status_code=404)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
