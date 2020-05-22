from abstractcollection import AbstractCollection
from btnode import BTNode
from linkedstack import LinkedStack


class LinkedBT(AbstractCollection):
    """
    An link-based binary tree implementation.
    """
    def __init__(self, source_collection=None):
        """
        (LinkedBT, Collection) -> NoneType
        Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present.
        """
        self._root = None
        AbstractCollection.__init__(self, source_collection)

    def __str__(self):
        """
        (LinkedBT) -> str
        Returns a string representation with the tree rotated
        90 degrees counterclockwise.
        """
        def recurse(node, level):
            s = ""
            if node is not None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self._root, 0)

    def __iter__(self):
        """
        (LinkedBT) -> data
        Supports a preorder traversal on a view of self.
        """
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right is not None:
                    stack.push(node.right)
                if node.left is not None:
                    stack.push(node.left)

    def add(self, item):
        """
        (LinkedBT, item) -> NoneType
        Adds item to the tree.
        """
        def recurse(node):
            if item < node.data:
                if node.left is None:
                    node.left = BTNode(item)
                else:
                    recurse(node.left)
            elif node.right is None:
                node.right = BTNode(item)
            else:
                recurse(node.right)

        if self.isEmpty():
            self._root = BTNode(item)
        else:
            recurse(self._root)
        self._size += 1
