class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:  # apple
            if char not in node.children:
                node.children[char] = TrieNode()  # create a new node
            node = node.children[char]  # move to a next node

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root  # start from a root node

        for char in word:
            if char not in node.children:  # can't find a char node
                return False
            node = node.children[char]  # move to a char node

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root  # start from a root node

        for char in prefix:
            if char not in node.children:  # can't find a char node
                return False
            node = node.children[char]  # move to a char node

        return True
