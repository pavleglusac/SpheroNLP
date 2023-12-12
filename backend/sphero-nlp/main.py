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
import asyncio

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

text_translator = ChatGPTTranslator()

async def execute_code(code_model):
    try:
        await asyncio.to_thread(exec, code_model.to_python())
    except Exception as e:
        print(e)
        return str(e)
    return "Success"


def language_model_to_json(obj, depth=0):
    if type(obj) in [int, float, str, bool]:
        return obj
    
    if type(obj) == list:
        return [language_model_to_json(elem, depth+1) for elem in obj]
    
    attrs = vars(obj)

    class_name = obj.__class__.__name__
    json_obj = {}
    for attr in attrs:
        if attr.startswith("_") or "parent" in attr:
            continue
        json_obj[attr] = language_model_to_json(attrs[attr], depth+1)

    json_obj["type"] = class_name
    json_obj["depth"] = depth
    return json_obj


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/translate")
async def generate(request: TranslationRequest):
    text = request.text
    code = text_translator.translate(text)
    code_model = parser.parse(code)
    return [code_model.to_javascript(), code_model.to_codeblocks(), language_model_to_json(code_model)]


@app.post("/execute")
async def execute(text=Body(embed=True)):
    print(f"User input: {text}")
    code = text_translator.translate(text)
    print("*"*50)
    print(code)
    code_model = parser.parse(code)
    await execute_code(code_model)
    return [code_model.to_javascript(), code_model.to_codeblocks(), language_model_to_json(code_model)]


if __name__ == "__main__":
    uvicorn.run(app, host="http://localhost", port=8000)