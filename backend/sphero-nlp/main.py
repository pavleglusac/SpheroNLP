from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi import Body, FastAPI
from translator.translators import ChatGPTTranslator, MockTranslator
from language import Language, parser
import sys

from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

text_translator = MockTranslator()

def execute_code(code_model):
    try:
        exec(code_model.to_python())
    except Exception as e:
        print(e)
        return str(e)
    return "Success"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/translate")
async def generate(request: TranslationRequest):
    text = request.text
    code = text_translator.translate(text)
    code_model = parser.parse(code)
    return [code_model.to_javascript(), code_model.to_codeblocks()]


@app.post("/execute")
async def execute(text=Body(embed=True)):
    code = text_translator.translate(text)
    code_model = parser.parse(code)
    execute_code(code_model)
    return [code_model.to_javascript(), code_model.to_codeblocks()]


if __name__ == "__main__":
    uvicorn.run(app, host="http://localhost", port=8000)