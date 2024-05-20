def vi_mode(word, vi_dict):
    """
    Searches for a word in the Vietnamese dictionary and returns its details and pronunciation.

    Arguments:
        word (str): The word to search for in the Vietnamese dictionary.
        vi_dict (Trie): The Vietnamese dictionary to search in.

    Returns:
        tuple: A tuple containing the details and pronunciation of the word if found, otherwise None.
    """
    data = vi_dict.search(word)
    if data is not None:
        details = data['details']
        pronunciation = data['pronunciation']
    else:
        details = None
        pronunciation = None
    return details, pronunciation

def en_mode(word, en_dict):
    """
    Searches for a word in the English dictionary and returns its details and pronunciation.

    Arguments:
        word (str): The word to search for in the English dictionary.
        en_dict (PyDictionary): The English dictionary to search in.

    Returns:
        tuple: A tuple containing the details and pronunciation of the word if found, otherwise None.
    """
    data = en_dict.meaning(word)
    details = []
    if data is not None:
        for part, meanings in data.items():
            details.append('* ' + part)
            for meaning in meanings:
                details.append('- ' + meaning)
    pronunciation = None
    return details, pronunciation

def load_history(history_file):
    """
    Loads and returns the search history from a file.

    Arguments:
        history_file (str): The file from which to load the search history.

    Returns:
        set: A set containing the search history.
    """
    with open(history_file, 'r') as h:
        history = h.read().splitlines()
    return history
