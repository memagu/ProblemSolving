from typing import Dict, List, Optional, Tuple
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


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)pass


if __name__ == "__main__":
    word_dictionary = WordDictionary()
    word_dictionary.addWord("bad")
    word_dictionary.addWord("dad")
    word_dictionary.addWord("mad")
    print(word_dictionary.word_dictionary)
    print(word_dictionary.search("pad"))  # return False
    print(word_dictionary.search("bad"))  # return True
    print(word_dictionary.search(".ad"))  # return True
    print(word_dictionary.search("b.."))  # return True
