from timer import timing

class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(root):
    if root is None:
        return 0
    else:
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        return max(left_depth, right_depth) + 1

# Example usage:
# Constructing a binary tree
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#   / \
#  8   9 


root = BinaryTreeNode()
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.left = BinaryTreeNode(8)
root.left.left.right = BinaryTreeNode(9)

@timing
def test_maxDepth():
    maxDepth(root)

test_maxDepth()


