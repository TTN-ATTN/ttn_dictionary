# Docstrings for ttn_dictionary

## Trie.py

### TrieNode
Trie Node class representing a node in the Trie data structure.

Attributes:
- **`children`** (dict): Dictionary to store child nodes.
- **`End`** (bool): Flag indicating whether the node represents the end of a word.
- **`data`** (any): Associated data for the node.

### Trie
Trie data structure implementation for storing and searching words.

Attributes:
- **`root`** (TrieNode): The root node of the Trie.

**`__init__(self)`**
- Initializes the Trie with a root node.

**`insert(self, word, data)`**
- Insert a word and its associated data into the Trie.
  - **Arguments:**
    - **`word`** (str): The word to be inserted into the Trie.
    - **`data`** (any): The associated data for the word.
  - **Returns:** None

**`search(self, word)`**
- Search for a word in the Trie and return its associated data if found.
  - **Arguments:**
    - **`word`** (str): The word to search for in the Trie.
  - **Returns:** The associated data for the word if found, otherwise None.

**`load_data(self, filename)`**
- Load data from a file into the Trie.
  - **Arguments:**
    - **`filename`** (str): The name of the file from which to load data into the Trie.
  - **Returns:** None

**`autocomplete(self, prefix)`**
- Provide autocomplete suggestions based on a given prefix.
  - **Arguments:**
    - **`prefix`** (str): The prefix string for which autocomplete suggestions are to be provided.
  - **Returns:** A list of autocomplete suggestions.

**`dfs(self, node, prefix, suggestions)`**
- Perform a depth-first search to find all words with the given prefix.
  - **Arguments:**
    - **`node`** (TrieNode): The current node in the Trie during the depth-first search.
    - **`prefix`** (str): The prefix string accumulated so far during the search.
    - **`suggestions`** (list): A list to store the autocomplete suggestions found during the search.
  - **Returns:** None

**`print_word(self, word)`**
- Print the details of a word if found in the Trie.
  - **Arguments:**
    - **`word`** (str): The word whose details are to be printed if found in the Trie.
  - **Returns:** None

---

## app.py

**`get_index(request: Request)`**
- Returns the index page.
  - **Arguments:**
    - **`request`**: The HTTP request object.
  - **Returns:** The HTML response for the index page.

**`search_word(request: Request, word: str = None, mode: str = 'vi')`**
- Searches for a word in the specified mode (Vietnamese or English) and returns the search results page.
  - **Arguments:**
    - **`request`**: The HTTP request object.
    - **`word`**: The word to search for (optional).
    - **`mode`**: The mode for the search, either 'vi' (Vietnamese) or 'en' (English). Default is 'vi'.
  - **Returns:** The HTML response for the search results page.

**`autocomplete_word(prefix: str)`**
- Returns a list of autocomplete suggestions for the given prefix.
  - **Arguments:**
    - **`prefix`**: The prefix string for which autocomplete suggestions are to be provided.
  - **Returns:** A JSON response containing the autocomplete suggestions.

---

## utils.py

**`vi_mode(word, vi_dict)`**
- Searches for a word in the Vietnamese dictionary and returns its details and pronunciation.
  - **Arguments:**
    - **`word`**: The word to search for in the Vietnamese dictionary.
    - **`vi_dict`**: The Vietnamese dictionary to search in.
  - **Returns:** A tuple containing the details and pronunciation of the word if found, otherwise None.

**`en_mode(word, en_dict)`**
- Searches for a word in the English dictionary and returns its details and pronunciation.
  - **Arguments:**
    - **`word`**: The word to search for in the English dictionary.
    - **`en_dict`**: The English dictionary to search in.
  - **Returns:** A tuple containing the details and pronunciation of the word if found, otherwise None.

**`load_history(history_file)`**
- Loads and returns the search history from a file.
  - **Arguments:**
    - **`history_file`**: The file from which to load the search history.
  - **Returns:** A list containing the search history.

---

## autocomplete.js

**`$(document).ready(function() {`**
- Initializes the autocomplete functionality when the document is ready.

**`$("#search-input").on("input", function() {`**
- Event handler for input event on #search-input element.
- Fetches autocomplete suggestions based on input prefix.
  - **Arguments:** None
  - **Returns:** None

**`$(document).on("click", "#autocomplete-list li", function() {`**
- Event handler for click event on dynamically created list items within #autocomplete-list.
- Populates the search input with the selected suggestion.
  - **Arguments:** None
  - **Returns:** None

---

## history.js

**`$(document).ready(function () {`**
- Initializes the history functionality when the document is ready.

**`$("#show-history").click(function () {`**
- Event handler for click event on #show-history element.
- Toggles the visibility of the #history-list element.
  - **Arguments:** None
  - **Returns:** None

**`$(document).on("click", ".history-item", function () {`**
- Event handler for click event on dynamically created .history-item elements.
- Sets the value of #search-input with the clicked word and hides the #history-list.
  - **Arguments:** None
  - **Returns:** None