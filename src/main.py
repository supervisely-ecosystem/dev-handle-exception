import os
from fastapi import FastAPI, Request
import supervisely as sly


app = FastAPI()
sly.app.fastapi.init(app)


@app.get("/")
async def read_index(request: Request):
    templates = sly.app.fastapi.Jinja2Templates(directory=os.getcwd())
    return templates.TemplateResponse("templates/index.html", {"request": request})


@app.post("/raise-exception-500")
async def generate(request: Request):
    print("hello")
    raise ValueError("123")
