class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # prepare dictionary to map the content to index of the out 
        content_map = defaultdict(int) # int, coz we store index
        out = []
        for i in paths:
            directory = i.split()
            for i in range(1,len(directory)):
                file = directory[i]
                content = file[file.find('('):-1]
                if content in content_map:
                    ind = content_map[content]
                    out[ind].append('/'.join([directory[0],file[:file.find('(')]]))
                else:
                    content_map[content] = len(out)
                    out.append(['/'.join([directory[0],file[:file.find('(')]])])
        
        return [i for i in out if len(i)>1]
                    