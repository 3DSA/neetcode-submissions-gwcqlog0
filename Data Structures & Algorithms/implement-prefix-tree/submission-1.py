class PrefixTree:
    def __init__(self):
        self.neighbors = {}
        self.isWord = False
        

    def insert(self, word: str) -> None:
        curr = self
        for s in word:
            curr.neighbors.setdefault(s, PrefixTree())
            curr = curr.neighbors[s]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self
        for s in word:
            if s in curr.neighbors:
                curr = curr.neighbors[s]
            else:
                return False
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for s in prefix:
            if s in curr.neighbors:
                curr = curr.neighbors[s]
            else:
                return False
        return True
        
        