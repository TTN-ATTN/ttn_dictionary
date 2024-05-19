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
    """
    Index page.
    
    Arguments:
        request: The HTTP request object.
        
    Returns: The HTML response for the index page.
    """
    return templates.TemplateResponse("index.html", {"request": request, "history": history[-20:]})

@app.get("/search", response_class=HTMLResponse)
async def search_word(request: Request, word: str = None, mode: str = 'vi'):
    """
    Searches for a word in the specified mode (Vietnamese or English) and returns the search results page.
    
    Arguments:
        request: The HTTP request object.
        word: The word to search for (optional).
        mode: The mode for the search, either 'vi' (Vietnamese) or 'en' (English). Default is 'vi'.
    
    Returns: The HTML response for the search results page.
    """
    word = word.strip()
    word = word.lower()
    history.append(word)
    with open(history_file, 'a') as h:
        h.write(word + '\n')
    
    if mode == 'vi':
        details, pronunciation = vi_mode(word, mydict)
    else:
        details, pronunciation = en_mode(word, en_dict)
        
    return templates.TemplateResponse(
        "result.html",
        {"request": request, "word": word.upper(), "pronunciation": pronunciation, "details": details, "history": history[-20:]},
    )

@app.get("/autocomplete")
async def autocomplete_word(prefix: str):
    """
    Autocomplete suggestions for the given prefix.
  
    Arguments:
        prefix: The prefix string for which autocomplete suggestions are to be provided.
    
    Returns: A JSON response containing the autocomplete suggestions.
    """
    suggestions = mydict.autocomplete(prefix.lower())
    return {"suggestions": suggestions[:20]}

