from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from PyDictionary import PyDictionary
from os.path import dirname, join, abspath
from app.Trie import *
from app.utils import vi_mode, en_mode, load_history

project_root = dirname(dirname(abspath(__file__)))
data_file = join(project_root, "database", "data_full.txt")
history_file = join(project_root, "database", "history.txt")

app = FastAPI()
templates = Jinja2Templates(directory="templates")

mydict = Trie()
mydict.load_data(data_file)
en_dict = PyDictionary()
history = load_history(history_file)

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    his = []
    for h in history:
        his.append(h)
    return templates.TemplateResponse("index.html", {"request": request, "history": his[:20]})

@app.get("/search", response_class=HTMLResponse)
async def search_word(request: Request, word: str = None, mode: str = 'vi'):
    word = word.strip()
    word = word.lower()
    
    if word not in history:
        with open(history_file, 'a') as h:
            h.write(word + '\n')
        history.add(word)

    his = []
    for h in history:
        his.append(h)
    
    if mode == 'vi':
        details, pronunciation = vi_mode(word, mydict)
    else:
        details, pronunciation = en_mode(word, en_dict)
        
    return templates.TemplateResponse(
        "result.html",
        {"request": request, "word": word.upper(), "pronunciation": pronunciation, "details": details, "history": his[:20]},
    )

@app.get("/autocomplete")
async def autocomplete_word(prefix: str):
    suggestions = mydict.autocomplete(prefix.lower())
    return {"suggestions": suggestions[:20]}

