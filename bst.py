
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)


def lowest_common_ancestor(bst, child1, child2):
    if child1 > bst.value and child2 > bst.value:
        return lowest_common_ancestor(bst.right, child1, child2)

    if child1 < bst.value and child2 < bst.value:
        return lowest_common_ancestor(bst.left, child1, child2)

    else:
        return bst.value


def lowest_common_ancestor_iterative(bst, child1, child2):
    node = bst
    while node is not None:
        if child1 > node.value and child2 > node.value:
            node = node.right

        if child1 < node.value and child2 < node.value:
            node = node.left

    return node.value


bst = BinarySearchTree(80)
for i in [85, 40, 30, 45, 1]:
    bst.insert(i)

print(lowest_common_ancestor(bst, 1, 45))
