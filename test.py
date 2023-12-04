import binarytree
from binarytree import BinaryTree

bt = BinaryTree(value=5)

bt.append(4)
bt.append(6)
bt.append(9)

print(f"{binarytree.pre_order(bt)}")
print(f"{binarytree.in_order(bt)}")
print(f"{binarytree.post_order(bt)}")

binarytree.print_tree(bt)
