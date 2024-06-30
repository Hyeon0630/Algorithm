from typing import Union

class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTreeNode(TreeNode):
    def __init__(self, key: int):
        super().__init__(key)
        self.color = "RED"

class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackTreeNode(None)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    def left_rotate(self, x: Union[TreeNode, RedBlackTreeNode]):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x: Union[TreeNode, RedBlackTreeNode]):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def rb_insert(self, z: RedBlackTreeNode):
        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = self.NIL
        z.right = self.NIL
        z.color = "RED"

        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z: RedBlackTreeNode):
        while z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "RED":
                    z.parent.color = "BLACK"  # Case 1
                    y.color = "BLACK"          # Case 1
                    z.parent.parent.color = "RED"  # Case 1
                    z = z.parent.parent         # Case 1
                else:
                    if z == z.parent.right:
                        z = z.parent              # Case 2
                        self.left_rotate(z)       # Case 2
                    z.parent.color = "BLACK"      # Case 3
                    z.parent.parent.color = "RED" # Case 3
                    self.right_rotate(z.parent.parent)  # Case 3
            else:
                y = z.parent.parent.left
                if y.color == "RED":
                    z.parent.color = "BLACK"  # Case 1
                    y.color = "BLACK"          # Case 1
                    z.parent.parent.color = "RED"  # Case 1
                    z = z.parent.parent         # Case 1
                else:
                    if z == z.parent.left:
                        z = z.parent              # Case 2
                        self.right_rotate(z)       # Case 2
                    z.parent.color = "BLACK"      # Case 3
                    z.parent.parent.color = "RED" # Case 3
                    self.left_rotate(z.parent.parent)  # Case 3
        self.root.color = "BLACK"  # Additional line for the root property

    def tree_delete(self, z: RedBlackTreeNode):
        if z.left == self.NIL or z.right == self.NIL:
            y = z
        else:
            y = self.tree_successor(z)
        if y.left != self.NIL:
            x = y.left
        else:
            x = y.right
        if x != self.NIL:
            x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        if y != z:
            z.key = y.key
            # 만약 y의 다른 데이터가 있으면 여기서 z로 복사해야 합니다.
        if y.color == "BLACK":
            self.rb_delete_fixup(x)
        return y

    def rb_delete_fixup(self, x: RedBlackTreeNode):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"

# Sample test
rbt = RedBlackTree()
keys_to_insert = [4, 1, 2, 3, 4]

# Insert keys
for key in keys_to_insert:
    rbt.rb_insert(RedBlackTreeNode(key))

print("Inorder traversal of the RBT:")
rbt.inorder_tree_walk(rbt.root)
