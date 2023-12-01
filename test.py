import binarytree
from binarytree import BinaryTree

bt = BinaryTree(5)

bt.append(4)
bt.append(6)

pre_order = binarytree.pre_order(bt)
in_order = binarytree.in_order(bt)
post_order = binarytree.post_order(bt)

print(f"{pre_order}")
print(f"{in_order}")
print(f"{post_order}")

binarytree.print_tree(bt)

