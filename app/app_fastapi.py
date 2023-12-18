from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import torch
import json

from app.model.model_func import load_model, load_tokenizer, DICT_SENTIMENT

model = None
tokenizer = None
app = FastAPI()


class TextClass(BaseModel):
    text: str
    inference: int


@app.on_event('startup')
def create_model():
    global model
    global tokenizer
    model = load_model()
    tokenizer = load_tokenizer()


@app.get("/")
def read_root():
    return 'Hello, FastAPI!'


@app.post('/clf_text')
def class_text(data: TextClass):

    tokenized_text = tokenizer(data.text, max_length=512, padding=True, truncation=True, return_tensors='pt')
    with torch.inference_mode():
        outputs = model(**tokenized_text)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
    predicted = torch.argmax(predicted, dim=1).item()

    data.inference = predicted

    return DICT_SENTIMENT[data.inference]