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
async def generate(text=Body(embed=True)):
    code = text_translator.translate(text)
    code_model = parser.parse(code)
    return str(code_model)


@app.post("/execute")
async def execute(text=Body(embed=True)):
    code = text_translator.translate(text)
    code_model = parser.parse(code)
    return execute_code(code_model)


if __name__ == "__main__":
    uvicorn.run(app, host="http://localhost", port=8000)