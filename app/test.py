from Trie import Trie, TrieNode
from os.path import *

trie = Trie()
trie.load_data(r"D:\CODE\ttn_dictionary\database\data_test.txt")
project_root = dirname(dirname(abspath(__file__)))
data_file = join(project_root, "database", "data_full.txt")
history_file = join(project_root, "database", "history.txt")

while True:
    print(data_file)
    print(history_file)
    word = input("Word for testing Trie: ")
    if word == "end testing":
        break
    trie.print_word(word)
