class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        book = defaultdict(int)
        for i in cpdomains:
            temp = i.split()
            users, domain = int(temp[0]), temp[1]
            
            dot = domain.find('.') 
            while dot != -1:
                book[domain] += users
                domain = domain[dot+1:]
                dot = domain.find('.')
            book[domain] += users
        
        output = []
        for key,value in zip(book.keys(),book.values()):
            tmp2 = [str(value),key]
            output.append(' '.join(tmp2))
        return output