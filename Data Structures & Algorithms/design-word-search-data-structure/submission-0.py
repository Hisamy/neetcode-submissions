class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:
    def __init__(self):
        self.node = TrieNode()
    
    def addWord(self, word: str) -> None:
        node = self.node
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endOfWord = True
        
    def search(self, word: str) -> bool:

        def dfs(j, root):
            node = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.endOfWord
        return dfs(0, self.node)


        



        
