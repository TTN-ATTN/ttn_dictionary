from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.Trie import Trie, TrieNode
from PyDictionary import PyDictionary

app = FastAPI()
templates = Jinja2Templates(directory="templates")
mydict = Trie()
mydict.load_data(r"D:\CODE\ttn_dictionary\database\data_full.txt")
en_dict = PyDictionary()

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    """Returns the index page."""
    return templates.TemplateResponse("index.html", {"request": request})

def vi_mode(word):
    """Searches for a word in the Vietnamese dictionary and returns its details and pronunciation."""
    data = mydict.search(word)
    if data is not None:
        details = data['details']
        pronunciation = data['pronunciation']
    else:
        details = None
        pronunciation = None
    return details, pronunciation

def en_mode(word):
    """Searches for a word in the English dictionary and returns its details and pronunciation."""
    data = en_dict.meaning(word)
    details = []
    if data is not None:
        for part, meanings in data.items():
            details.append('* ' + part)
            for meaning in meanings:
                details.append('- ' + meaning)
    pronunciation = None
    return details, pronunciation

@app.get("/search", response_class=HTMLResponse)
async def search_word(request: Request, word: str = None, mode: str = 'vi'):
    """Searches for a word in the specified mode (Vietnamese or English) and returns the search results page."""
    word = word.lower()
    
    if mode == 'vi':
        details, pronunciation = vi_mode(word)
    else:
        details, pronunciation = en_mode(word)
        
    return templates.TemplateResponse(
        "result.html",
        {"request": request, "word": word.upper(), "pronunciation": pronunciation, "details": details},
    )

@app.get("/autocomplete")
async def autocomplete_word(prefix: str):
    """Returns a list of autocomplete suggestions for the given prefix."""
    suggestions = mydict.autocomplete(prefix.lower())
    return {"suggestions": suggestions}
