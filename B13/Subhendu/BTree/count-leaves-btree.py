def countLeaves(root):
    # Code here
    ### https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1
    res= []
    def solve(node):
        if not root:
            return
        if node.left is None and node.right is None:
            res.append(node.data)
            return
        if node.left:
            solve(node.left)
        if node.right:
            solve(node.right)
    solve(root)
    return len(res)