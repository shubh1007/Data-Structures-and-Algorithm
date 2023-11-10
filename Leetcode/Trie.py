class TrieNode:
    def __init__(self) -> None:
        self.children = [None for _ in range(26)]
        self.isEndOfWord = False

class Trie:
    
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.isEndOfWord = True
    
    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                return False
            current = current.children[index]
        return current.isEndOfWord


class WordDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.dfs(word, 0, self.trie.root)
    
    def dfs(self, word: str, index: int, node: TrieNode) -> bool:
        if index == len(word):
            return node.isEndOfWord
        
        if word[index] == '.':
            for child in node.children:
                if child and self.dfs(word, index + 1, child):
                    return True
            return False
        else:
            index = ord(word[index]) - ord('a')
            if not node.children[index]:
                return False
            return self.dfs(word, index + 1, node.children[index])


# # Path: Solution.py
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         trie = Trie()
#         for word in words:
#             trie.insert(word)
        
#         result = set()
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 self.dfs(board, i, j, trie.root, result, '')
#         return list(result)
    
#     def dfs(self, board: List[List[str]], i: int, j: int, node: TrieNode, result: set, word: str) -> None:
#         if node.isEndOfWord:
#             result.add(word)
        
#         if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
#             return
        
#         temp = board[i][j]
#         index = ord(temp) - ord('a')
#         if not node.children[index]:
#             return
        
#         board[i][j] = '#'
#         self.dfs(board, i + 1, j, node.children[index], result, word + temp)
#         self.dfs(board, i - 1, j, node.children[index], result, word + temp)
#         self.dfs(board, i, j + 1, node.children[index], result, word + temp)
#         self.dfs(board, i, j - 1, node.children[index], result, word + temp)
#         board[i][j] = temp