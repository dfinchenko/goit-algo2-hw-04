from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not all(isinstance(s, str) for s in strings):
            raise TypeError("All elements in strings must be of type str")
        if not strings:
            return ""

        for word in strings:
            self.put(word)

        def find_lcp(node):
            prefix = ""
            while node and len(node.children) == 1 and node.value is None:
                char = next(iter(node.children))
                prefix += char
                node = node.children[char]
            return prefix

        return find_lcp(self.root)
    
if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""