class WordDictionary:

    def __init__(self):
        self.neighbors = {}
        self.Word = False

    def addWord(self, word: str) -> None:
        curr = self
        for s in word:
            curr.neighbors.setdefault(s, WordDictionary())
            curr = curr.neighbors[s]
        curr.Word = True
        

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            if word[i] in curr.neighbors:
                curr = curr.neighbors[word[i]]
            elif word[i] == ".":
                for chars in curr.neighbors:
                    temp = curr.neighbors[chars]
                    if temp.search(word[i+1:]):
                        return True
                return False
            else:
                return False
        return curr.Word
        
