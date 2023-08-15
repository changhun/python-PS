class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

    def insert(self, s:str):
        if not s:
            self.word = True
            return
        if not s[0] in self.children:
            self.children[s[0]] = TrieNode();
        self.children[s[0]].insert(s[1:])

    def search(self, s:str):
        if not s:
            return self.word
        if s[0] not in self.children:
            return False
        return self.children[s[0]].search(s[1:])

    def startsWith(self, s:str):
        if not s:
            return True
        if not s[0] in self.children:
            return False
        return self.children[s[0]].startsWith(s[1:])


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        self.root.insert(s)
    def search(self, s):
        return self.root.search(s)
    def startsWith(self, s):
        return self.root.startsWith(s)


trie = Trie()
trie.insert("apple")
ret = trie.startsWith("app")
print(ret)