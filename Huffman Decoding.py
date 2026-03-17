def decode_huffman(root,encoded):
    
    res=""
    node=root
    
    for bit in encoded:
        if bit=='0':
            node=node.left
        else:
            node=node.right
        
        if node.char:
            res+=node.char
            node=root
    
    return res
