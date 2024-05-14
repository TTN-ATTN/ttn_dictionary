''' Tesing Trie functionality'''

from Trie import Trie, TrieNode

trie = Trie()
trie.load_data(r"D:\CODE\ttn_dictionary\database\data_test.txt")

while True:
    word = input("Word for testing Trie: ")
    trie.print_word(word)
    if word == "end testing":
        break