# Docstrings for ttn_dictionary

## Trie.py

### TrieNode
#### Node structure for Trie.

**`__init__(self)`**
- Initializes the attributes of the `TrieNode`.

### Trie
#### Trie data structure, consisting of several methods.

**`__init__(self)`**
- Initializes the Trie with a root node.

**`insert(self, word, data)`**
- Inserts a word and its associated data into the Trie.
- **Arguments:**
  - **`word`**: The word to be inserted into the Trie.
  - **`data`**: The associated data for the word.

**`search(self, word)`**
- Searches for a word in the Trie and returns its data if found.
- **Arguments:**
  - **`word`**: The word to search for in the Trie.

**`load_data(self, filename)`**
- Loads data from a file into the Trie.
- **Arguments:**
  - **`filename`**: The name of the file from which to load data into the Trie.

**`autocomplete(self, prefix)`**
- Provides autocomplete suggestions based on a given prefix.
- **Arguments:**
  - **`prefix`**: The prefix string for which autocomplete suggestions are to be provided.

**`dfs(self, node, prefix, suggestions)`**
- Performs a depth-first search to find all words with the given prefix.
- **Arguments:**
  - **`node`**: The current node in the Trie during the depth-first search.
  - **`prefix`**: The prefix string accumulated so far during the search.
  - **`suggestions`**: A list to store the autocomplete suggestions found during the search.

**`print_word(self, word)`**
- Prints the details of a word if found in the Trie. This is for testing in `test.py`.
- **Arguments:**
  - **`word`**: The word whose details are to be printed if found in the Trie.

---

## app.py

**`get_index(request: Request)`**
- Returns the index page.
- **Arguments:**
  - **`request`**: The HTTP request object.

**`search_word(request: Request, word: str = None, mode: str = 'vi')`**
- Searches for a word in the specified mode (Vietnamese or English) and returns the search results page.
- **Arguments:**
  - **`request`**: The HTTP request object.
  - **`word`**: The word to search for (optional).
  - **`mode`**: The mode for the search, either 'vi' (Vietnamese) or 'en' (English). Default is 'vi'.

**`autocomplete_word(prefix: str)`**
- Returns a list of autocomplete suggestions for the given prefix.
- **Arguments:**
  - **`prefix`**: The prefix string for which autocomplete suggestions are to be provided.

---

## utils.py

**`vi_mode(word, vi_dict)`**
- Searches for a word in the Vietnamese dictionary and returns its details and pronunciation.
- **Arguments:**
  - **`word`**: The word to search for in the Vietnamese dictionary.
  - **`vi_dict`**: The Vietnamese dictionary to search in.

**`en_mode(word, en_dict)`**
- Searches for a word in the English dictionary and returns its details and pronunciation.
- **Arguments:**
  - **`word`**: The word to search for in the English dictionary.
  - **`en_dict`**: The English dictionary to search in.

**`load_history(history_file)`**
- Loads and returns the search history from a file.
- **Arguments:**
  - **`history_file`**: The file from which to load the search history.
