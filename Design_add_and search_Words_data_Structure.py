class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
    
    def search(self, word):
        def dfs(start, root):
            current=root
            for i in range(len(word)):
                w=word[i]
                if w==".":
                    for child in current.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if w not in current.children:
                        return False
                    current=current.children[w]
            return current.isEnd
        return dfs(0,self.root)
      
if __name__ == "__main__":
    s=WordDictionary()
    s.addWord("bad")
    s.addWord("dad")
    s.addWord("mad")
    print(s.search("pad"))
    print(s.search("bad"))
    print(s.search(".ad"))
    print(s.search("b.."))
        
      