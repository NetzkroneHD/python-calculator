from __future__ import annotations


class BinaryTree:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left: BinaryTree | None = left
        self.right: BinaryTree | None = right

    def is_empty(self) -> bool:
        return self.value is None

    def append(self, value):
        append(self, value)

    def remove(self, value):
        return remove(self, value)

    def smallest(self):
        return smallest(self)

    def largest(self):
        return largest(self)

    def search(self, value):
        return search(self, value)

    def contains(self, value) -> bool:
        return contains(self, value)

    def size(self) -> int:
        return size(self)

    def depth(self) -> int:
        return depth(self)

    def width(self) -> int:
        return width(self)

    def get_row(self, row: int):
        return get_row(self, row)

    def __str__(self):
        return f"(value={self.value}, left={self.left}, right={self.right})"


class TreeSize:

    def __init__(self, size: int):
        self.size = size


def smallest(leaf: BinaryTree) -> BinaryTree:
    current: BinaryTree = leaf

    while current.left is not None:
        current = current.left
    return current


def largest(leaf: BinaryTree) -> BinaryTree:
    current: BinaryTree = leaf

    while current.right is not None:
        current = current.right
    return current


def append(leaf: BinaryTree, value):
    if leaf.is_empty():
        leaf.value = value
    else:
        if value < leaf.value:
            if leaf.left is None:
                leaf.left = BinaryTree(value, None, None)
            else:
                append(leaf.left, value)
        elif value > leaf.value:
            if leaf.right is None:
                leaf.right = BinaryTree(value, None, None)
            else:
                append(leaf.right, value)


def remove(leaf: BinaryTree, value):
    if leaf is None:
        return leaf

    # value liegt im linken Baum
    if value < leaf.value:
        leaf.left = remove(leaf.left, value)

    # value liegt im rechten Baum
    elif value > leaf.value:
        leaf.right = remove(leaf.right, value)

    # Element gefunden
    else:
        # Element mit nur einem Baum oder gar keinem
        if leaf.left is None:
            temp = leaf.right
            return temp

        elif leaf.right is None:
            temp = leaf.left
            return temp

        # Baum mit zwei Elementen
        # inorder kleinster Unterbaum
        temp = smallest(leaf.right)
        leaf.value = temp.value
        leaf.right = remove(leaf.right, temp.value)
    return leaf


def size(tree: BinaryTree) -> int:
    tree_size: TreeSize = TreeSize(0)
    __size(tree, tree_size)
    return tree_size.size


def width_left(tree: BinaryTree) -> int:
    width = 0
    node: BinaryTree = tree

    while node is not None and not node.is_empty():
        width += 1
        node = node.left

    return width


def width_right(tree: BinaryTree) -> int:
    width = 0
    node: BinaryTree = tree

    while node is not None and not node.is_empty():
        width += 1
        node = node.right

    return width


def width(tree: BinaryTree) -> int:
    return width_left(tree) + width_right(tree)


def depth(tree: BinaryTree) -> int:
    if (tree is None) or (tree.is_empty()):
        return 0

    left_height = depth(tree.left)
    right_height = depth(tree.right)

    return max(left_height, right_height) + 1


def search(tree: BinaryTree, value):
    if (tree is None) or (tree.is_empty()): return None

    if value < tree.value:
        return search(tree.left, value)
    elif value > tree.value:
        return search(tree.right, value)
    elif value == tree.value:
        return tree.value


def contains(tree: BinaryTree, value) -> bool:
    return search(tree, value) is not None


def pre_order(tree: BinaryTree, callback=None) -> list:
    values: list = []
    __pre_order(tree, values, callback)
    return values


def in_order(tree: BinaryTree, callback=None) -> list:
    values: list = []
    __in_order(tree, values, callback)
    return values


def post_order(tree: BinaryTree, callback=None) -> list:
    values: list = []
    __post_order(tree, values, callback)
    return values


def to_matrix(tree: BinaryTree) -> list:
    # matrix = [[0 for x in range(width)] for y in range(height)]
    tree_depth = depth(tree)
    tree_width = width(tree)

    matrix = [[0 for _ in range(tree_width)] for _ in range(tree_depth)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"[{i}][{j}] = {j}")

    return matrix


def get_row(tree: BinaryTree, row: int) -> list[BinaryTree]:
    trees: list[BinaryTree] = []
    __get_row(tree, row, TreeSize(0), trees)
    return trees


def __get_row(tree: BinaryTree, row: int, size: TreeSize, tree_list: list[BinaryTree]) -> list[BinaryTree]:
    if (tree is None) or (tree.is_empty()):
        return tree_list
    if row == size.size:
        tree_list.append(tree)
    else:
        size.size = size.size + 1
        __get_row(tree.left, row, size, tree_list)
        __get_row(tree.right, row, size, tree_list)

    return tree_list


def print_tree(root: BinaryTree):
    space = 0
    height = 2
    __print_tree(root, space, height)


def __print_tree(root: BinaryTree, space, height):
    # Wurzel
    if root is None:
        return

    # Distanz zwischen level erhöhen
    space += height

    # rechter Baum zuerst
    __print_tree(root.right, space, height)
    print()

    # Momentaner Baum, nachdem der Platz eingefügt wurde
    for i in range(height, space):
        print(' ', end='')

    print(root.value, end='')

    # linker Baum
    print()
    __print_tree(root.left, space, height)


# N-L-R
def __pre_order(tree: BinaryTree, values: list, callback=None) -> list:
    if (tree is None) or (tree.is_empty()):
        return []
    else:
        values.append(tree.value)
        if callback is not None:
            callback(tree)
        __pre_order(tree.left, values)
        __pre_order(tree.right, values)


# L-N-R
def __in_order(tree: BinaryTree, values: list, callback=None) -> list:
    if (tree is None) or (tree.is_empty()):
        return []
    else:
        __in_order(tree.left, values)
        values.append(tree.value)
        if callback is not None:
            callback(tree)
        __in_order(tree.right, values)


# L-R-N
def __post_order(tree: BinaryTree, values: list, callback=None) -> list:
    if (tree is None) or (tree.is_empty()):
        return []
    else:
        __post_order(tree.left, values)
        __post_order(tree.right, values)
        if callback is not None:
            callback(tree)
        values.append(tree.value)


def __size(tree: BinaryTree, size: TreeSize):
    if (tree is None) or (tree.is_empty()):
        return
    else:
        size.size = size.size + 1
        __size(tree.left, size)
        __size(tree.right, size)