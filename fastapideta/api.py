
from nltk.corpus import wordnet as wn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    word: str

def unique(words):
    return list(set(words))

def preprocessWord(word):
    return word.replace("_", " ") if "_" in word else word

@app.post('/wordnet')
def create_wordnet(data: Data):
    word = data.word
    synsets = wn.synsets(word)
    synonyms, antonyms, definition = list(), list(), list()
    try:
        definition.append(synsets[0].definition())
    except: pass
    for synset in synsets:
        for lemma in synset.lemmas():
            synonyms.append(preprocessWord(lemma.name()))
            if lemma.antonyms():
                antonyms.append(preprocessWord(lemma.antonyms()[0].name()))
    results = {'synonyms': unique(synonyms), 'antonyms': unique(antonyms), 'definition': definition}
    return JSONResponse(jsonable_encoder(results))