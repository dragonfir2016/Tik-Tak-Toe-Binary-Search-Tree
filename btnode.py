class BTNode:
    """
    Represents a node for a linked binary tree.
    """
    def __init__(self, data, left=None, right=None):
        """
        (BTNode, data, BTNode, BTNode) -> NoneType
        Creates a new object of BTNode class.
        """
        self.data = data
        self.left = left
        self.right = right
