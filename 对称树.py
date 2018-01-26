'''

给定一个二叉树，检查它是否是它自己的镜像（即围绕它的中心对称）。

例如，这个二叉树[1,2,2,3,4,4,3]是对称的：

    1
   / \
  2   2
 / \ / \
3  4 4  3
但以下[1,2,2,null,3,null,3] 不是：
    1
   / \
  2   2
   \   \
   3    3
注意：
如果你可以递归地和迭代地解决它，奖励点。

'''

def is_Mirror(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val == right.val:
        outPair = is_Mirror(left.left, right.right)
        inPair = is_Mirror(left.right, right.left)
        return outPair and inPair
    else:
        return False