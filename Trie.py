class TrieNode:
    def __init__(self):
        self.children={}
        self.endofword=False


class Trie:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        curr=self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr=curr.children[char]
        curr.endofword=True



    def search(self, word: str) -> bool:
        curr=self.root
        for char in word:
            if char not in curr.children:
                return False
            curr=curr.children[char]
        return curr.endofword
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr=curr.children[char]
        return True


#Your Trie object will be instantiated and called as such:
word1, word2, prefix1="apple", "app", "app"
obj = Trie()
obj.insert(word1)
param_2 = obj.search(word1)
param_3 = obj.search(word2)
param_4 = obj.startsWith(prefix1)
obj.insert(word2)
param_5 = obj.search(word2)

def main():
    print(param_2)
    print(param_3)
    print(param_4)
    print(param_5)

if __name__ == '__main__':
    main()