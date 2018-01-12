def checkBST(node, leftData=None, rightData=None):
	if not node:
		return True
	if leftData and node.data >= leftData:
		return False
	if rightData and node.data <= rightData:
		return False
	return checkBST(node.left, node.data, rightData)
		and checkBST(node.right, leftData, node.data)



def checkBST(n, min=0, max=10000):
    if not n:
        return True
    if n.data <= min or n.data >= max:
        return False
    return checkBST(n.left, min, n.data) and checkBST(n.right, n.data, max)