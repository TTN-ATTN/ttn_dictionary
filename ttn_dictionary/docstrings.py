"""Trie.py

TrieNode()
    Node structure for Trie.

    __init__(self)
        init the attributes of the TrieNode()

Trie()
    Trie data structure, consisting of __init__(), insert(), search(), load_data(), autocomplete(), dfs(), print_word()

    ___init___(self)
        Initialize Trie with a root node.

    insert(self, word, data)
        Insert a word and its associated data into the Trie.

    search(self, word)
        Search for a word in the Trie and return its data if found.

    load_data(self, filename)
        Load data from a file into the Trie.

    autocomplete(self, prefix)
        Provide autocomplete suggestions based on a given prefix.

    dfs(self, node, prefix, suggestions)
        Depth-first search to find all words with the given prefix.

    print_word(self, word)
        Print the details of a word if found in the Trie. This is for testing in test.py

"""

"""app.py

get_index(request: Request)
    Returns the index page.

search_word(request: Request, word: str = None, mode: str = 'vi')
    Searches for a word in the specified mode (Vietnamese or English) and returns the search results page.

autocomplete_word(prefix: str)
    Returns a list of autocomplete suggestions for the given prefix.

"""


"""utils.py

vi_mode(word, vi_dict):
    Searches for a word in the Vietnamese dictionary and returns its details and pronunciation.

en_mode(word, en_dict):
    Searches for a word in the English dictionary and returns its details and pronunciation.

load_history(history_file):
    Loads and returns the search history from a file.
    
"""
