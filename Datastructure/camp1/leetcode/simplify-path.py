class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        paths = path.split("/")
        # print(paths)
        for p in paths:
            if res and p == '..':
                res.pop()
                
            elif not p or p == '.' or p == '..':
                continue
            else:
                res.append(p)
        
        return "/" + "/".join(res)