class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def find(self, word: str) -> str:
        node = self.root
        for char in word:
            # if there are no words matching in trie, return argument
            if char not in node.children:
                return word
            node = node.children[char]  # move to a char node
            if node.is_end:
                print(node)
                return node

        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # insert root words to a trie
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        # check sentence by word, searching if exists in trie
        answer = []
        for word in sentence:
            replaced = trie.find(word)
            answer.append(replaced)

        return ' '.join(answer)


if __name__ == '__main__':
    replaceWords(dictionary=["a", "b", "c"],
                 sentence="aadsfasf absbs bbab cadsfafs")
