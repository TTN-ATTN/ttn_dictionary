def vi_mode(word, vi_dict):
    data = vi_dict.search(word)
    if data is not None:
        details = data['details']
        pronunciation = data['pronunciation']
    else:
        details = None
        pronunciation = None
    return details, pronunciation

def en_mode(word, en_dict):
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
    with open(history_file, 'r') as h:
        history = h.read().splitlines()
    return set(history)
