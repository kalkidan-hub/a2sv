class ListNode:
    def __init__(self,val,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.currentpage = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.currentpage.next = ListNode(url,self.currentpage)
        self.currentpage = self.currentpage.next

    def back(self, steps: int) -> str:
        while self.currentpage.prev and steps:
            self.currentpage = self.currentpage.prev
            steps -= 1
        return self.currentpage.val      
        

    def forward(self, steps: int) -> str:
        while self.currentpage.next and steps:
            self.currentpage = self.currentpage.next
            steps -= 1
        return self.currentpage.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)