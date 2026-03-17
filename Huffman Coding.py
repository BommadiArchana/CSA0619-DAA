import heapq

class Node:
    def __init__(self,freq,char=None,left=None,right=None):
        self.freq=freq
        self.char=char
        self.left=left
        self.right=right
        
    def __lt__(self,other):
        return self.freq<other.freq


def huffman(chars,freq):
    
    heap=[Node(freq[i],chars[i]) for i in range(len(chars))]
    heapq.heapify(heap)
    
    while len(heap)>1:
        l=heapq.heappop(heap)
        r=heapq.heappop(heap)
        heapq.heappush(heap,Node(l.freq+r.freq,None,l,r))
    
    root=heap[0]
    codes={}
    
    def dfs(node,code):
        if node.char:
            codes[node.char]=code
            return
        
        dfs(node.left,code+"0")
        dfs(node.right,code+"1")
    
    dfs(root,"")
    
    return codes


chars=['a','b','c','d']
freq=[5,9,12,13]

print(huffman(chars,freq))
