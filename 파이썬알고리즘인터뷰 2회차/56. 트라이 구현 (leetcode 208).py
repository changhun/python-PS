class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word : str):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.word = True


    def search(self, word : str):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.word

    def startsWith(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
