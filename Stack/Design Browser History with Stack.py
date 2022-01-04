"""Il y a pleins de manières de résoudre ce problème, par exemple avec une Linked List. Mais ici j'ai utilisé un stack.
résultat : 11% plus rapide, la mémoire osef parce que la première fois que j'ai run j'étais 28% et ensuite je suis passé 78% """ 


class History:
    def __init__(self, start):
        self.forward=[]
        self.backward=[]
        self.current = start

class BrowserHistory:

    def __init__(self, homepage: str):
        self.start=History(homepage)
    
    def visit(self, url: str) -> None:
        historique=self.start
        historique.forward=[]
        historique.backward.append(historique.current)
        historique.current=url

    def back(self, steps: int) -> str:
        historique=self.start
        while steps>0:
            if len(historique.backward)==0:
                return historique.current
            historique.forward.append(historique.current)
            historique.current=historique.backward.pop()
            steps-=1
        return historique.current

    def forward(self, steps: int) -> str:
        historique=self.start
        while steps>0:
            if len(historique.forward)==0:
                return historique.current
            historique.backward.append(historique.current)
            historique.current=historique.forward.pop()
            steps-=1
        return historique.current


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)