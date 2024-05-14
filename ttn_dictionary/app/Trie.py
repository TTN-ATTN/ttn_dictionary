class TrieNode:
    """Node structure for Trie."""
    def __init__(self):
        self.children = {}
        self.End = False
        self.data = None


class Trie:
    """Trie data structure."""
    def __init__(self):
        """Initialize Trie with a root node."""
        self.root = TrieNode()

    def insert(self, word, data):
        """Insert a word and its associated data into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.End = True
        if node.data is not None:
            node.data['details'].extend(data['details'])
        else:
            node.data = data

    def search(self, word):
        """Search for a word in the Trie and return its data if found."""
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        if node.End:
            return node.data
        return None

    def load_data(self, filename):
        """Load data from a file into the Trie."""
        with open(filename, 'r', encoding='utf-8') as file:
            word = None
            word_data = {}
            for line in file:
                line = line.strip()
                if line.startswith('@'):
                    if word:
                        self.insert(word, word_data)
                    parts = line[1:].split('/', 1)
                    word = parts[0].strip()
                    word_data = {'pronunciation': parts[1].strip() if len(parts) > 1 else None, 'details': []}
                elif word:
                    word_data['details'].append(line)
            if word:
                self.insert(word, word_data)

    def autocomplete(self, prefix):
        """Provide autocomplete suggestions based on a given prefix."""
        node = self.root
        suggestions = []
        for char in prefix:
            if char not in node.children:
                return suggestions
            node = node.children[char]
        self.dfs(node, prefix, suggestions)
        return suggestions

    def dfs(self, node, prefix, suggestions):
        """Depth-first search to find all words with the given prefix."""
        if node.End:
            suggestions.append(prefix)
        for char, child_node in node.children.items():
            self.dfs(child_node, prefix + char, suggestions)

    def print_word(self, word):
        """Print the details of a word if found in the Trie. This is for testing in test.py"""
        data = self.search(word)
        if data:
            print(word)
            if data['pronunciation'] is not None:
                print(f"/{data['pronunciation']}")
            for detail in data['details']:
                print(detail)
        else:
            print(f"{word} not found in the dictionary.")
