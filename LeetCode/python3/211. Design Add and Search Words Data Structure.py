from typing import Dict, List, Optional, Tuple

"""
from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self.word_dictionary = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.word_dictionary[frozenset(word)].add(word)

    def search(self, word: str) -> bool:

        if '.' not in word:
            word_letters = frozenset(word)

            if word_letters not in self.word_dictionary:
                return False

            if word in self.word_dictionary[word_letters]:
                return True

            return False

        word_letters = frozenset(char for char in word if char != '.')

        for letters, words in self.word_dictionary.items():
            if not word_letters.issubset(letters):
                continue

            for dict_word in words:
                if len(dict_word) != len(word):
                    continue

                for i, char in enumerate(word):
                    if char == '.':
                        continue

                    if char != dict_word[i]:
                        break

                else:
                    return True

        return False
"""

"""
from collections import deque


class WordDictionary:
    def __init__(self):
        self.children = {}
        self.word_terminator = False

    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()

            node = node.children[char]

        node.word_terminator = True

    def search(self, word: str) -> bool:
        queue = deque((self,))
        for depth, char in enumerate(word, 1):
            if not queue:
                return False

            for _ in range(len(queue)):
                node = queue.popleft()

                if char == '.':
                    for child in node.children.values():
                        if child.word_terminator and depth == len(word):
                            return True

                        queue.append(child)

                    continue

                if char in node.children:
                    child = node.children[char]
                    if child.word_terminator and depth == len(word):
                        return True

                    queue.append(child)

        return False
"""

"""
class WordDictionary:
    def __init__(self):
        self.word_trie = (False, -1, {})  # (word_terminator: bool, longest_word_from_here: int, children: dict)

    def addWord(self, word: str) -> None:
        node = self.word_trie
        for i, char in enumerate(word):
            word_terminator = i == len(word) - 1
            children = node[2]
            if char not in children:
                child = (word_terminator, len(word) - i, {})
                children[char] = child

            else:
                child = children[char]
                word_terminator = child[0] or i == len(word) - 1
                longest_word_from_here = child[1]
                if len(word) - i > child[1]:
                    longest_word_from_here = len(word) - i

                child = (word_terminator, longest_word_from_here, child[2])
                children[char] = child

            node = child

    def search(self, word: str) -> bool:
        queue = [(self.word_trie, 0)]
        while queue:
            node, depth = queue.pop()
            if depth == len(word):
                if node[0]:
                    return True
                continue

            required_word_length = len(word) - depth
            char = word[depth]
            children = node[2]

            if char == '.':
                for child in children.values():
                    if required_word_length > child[1] or required_word_length <= 0:
                        continue

                    if depth + 1 <= len(word):
                        queue.append((child, depth + 1))

                continue

            if char in children:
                child = children[char]
                if required_word_length > child[1] or required_word_length <= 0:
                    continue

                depth += 1
                if depth <= len(word):
                    queue.append((child, depth))

        return False
"""


class WordDictionary:
    def __init__(self):
        self.word_trie = (False, -1, {})  # (word_terminator: bool, longest_word_from_here: int, children: dict)

    def addWord(self, word: str) -> None:
        node = self.word_trie
        for i, char in enumerate(word):
            word_terminator = i == len(word) - 1
            children = node[2]
            if char not in children:
                child = (word_terminator, len(word) - i, {})
                children[char] = child
            else:
                child = children[char]
                word_terminator = child[0] or word_terminator
                longest_word_from_here = max(child[1], len(word) - i)
                child = (word_terminator, longest_word_from_here, child[2])
                children[char] = child

            node = child

    def search(self, word: str) -> bool:
        queue = [(self.word_trie, 0)]
        while queue:
            node, depth = queue.pop()
            if depth == len(word):
                if node[0]:
                    return True
                continue

            required_word_length = len(word) - depth
            char = word[depth]
            children = node[2]

            if char == '.':
                for child in children.values():
                    if required_word_length <= child[1] > 0:
                        queue.append((child, depth + 1))
                continue

            if char in children:
                child = children[char]
                if required_word_length <= child[1] > 0:
                    queue.append((child, depth + 1))

        return False

    # Your WordDictionary object will be instantiated and called as such:
    # obj = WordDictionary()
    # obj.addWord(word)
    # param_2 = obj.search(word)pass


if __name__ == "__main__":
    word_dictionary = WordDictionary()
    word_dictionary.addWord("bad")
    word_dictionary.addWord("dad")
    word_dictionary.addWord("mad")
    word_dictionary.addWord("madder")
    word_dictionary.addWord("mint")
    word_dictionary.addWord("mold")
    # print(word_dictionary.word_dictionary)
    print(word_dictionary.search("pad"))  # return False
    print(word_dictionary.search("bad"))  # return True
    print(word_dictionary.search(".ad"))  # return True
    print(word_dictionary.search("b.."))  # return True
    print(word_dictionary.search(".....r"))  # return True
    print(word_dictionary.search("..d"))  # return True
    print(word_dictionary.search("..e"))  # return False
