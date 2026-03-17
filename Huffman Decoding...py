def decode_huffman(root, encoded):

    result = ""
    node = root

    for bit in encoded:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        # check if leaf node
        if node.left is None and node.right is None:
            result += node.char
            node = root

    return result
