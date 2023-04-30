from typing import List
from collections import defaultdict
import collections

""" reversed test"""
"""
def check_palindrome(word: list) -> bool:
    print(word)
    rev = reversed(word)
    print(rev)
    
    print(reversed(word))
    return word == reversed(word)
    
    
#word = ['a', 'b', 'a']
#ret = check_palindrome(word)
print(ret)    
"""

""" str reverse test """
"""
def check_palindrome_str(word: str) -> bool:
    #return word == reversed(word)
    #return word == str(reversed(word))

    word_list = list(word)
    return word_list == list(reversed(word_list))
    
    
word = "aba"
ret = check_palindrome_str(word)

print(ret)    
"""


def check_palindrome_list(word: list) -> bool:
    return word == list(reversed(word))

def check_palindrome_str(word: str) -> bool:
    word_list = list(word)
    return word_list == list(reversed(word_list))


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        node = self.root
        for char in word:
            node = node.children[char]

        node.word = True
        node.index = index


    def check_palindrome(self, word: str, i: int):
        node = self.root
        ret = []
        for j, char in enumerate(word):
            if node.word and node.index != i:
                if check_palindrome_str(word[j:]):
                    ret.append([i, node.index])

            if char not in node.children:
                return ret
            node = node.children[char]


        def dfs(node: TrieNode):
            if node.word and node.index != i:
                if check_palindrome_list(remain_str):
                    ret.append([i, node.index])

            for char, next_node in node.children.items():
                remain_str.append(char)
                dfs(next_node)
                remain_str.pop()

        remain_str = []
        dfs(node)

        return ret


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie_root = Trie()
        ans = []

        for i, word in enumerate(words):
            rev_str = list(reversed(list(word)))
            #print(rev_str)
            rev_str = ''.join(rev_str)
            #print(rev_str)
            trie_root.insert(rev_str, i)
            #trie_root.insert(''.join(list(word).reverse()), i)

        for i, word in enumerate(words):
            ret = trie_root.check_palindrome(word, i)
            if len(ret) > 0:
                ans += ret

        return ans


words = ["bat","tab","cat"]
words = ["abcd","dcba","lls","s","sssll"]
ret = Solution().palindromePairs(words)
print(ret)