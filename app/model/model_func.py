import torch
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast

CHECKPOINT = 'blanchefort/rubert-base-cased-sentiment'

DICT_SENTIMENT = {
    0: 'NEUTRAL',
    1: 'POSITIVE',
    2: 'NEGATIVE'
}


def load_model():

    model = AutoModelForSequenceClassification.from_pretrained(CHECKPOINT, return_dict=True)
    return model


def load_tokenizer():

    tokenizer = BertTokenizerFast.from_pretrained(CHECKPOINT)
    return tokenizer