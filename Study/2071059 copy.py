class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.NIL = TreeNode(None)
        self.root = self.NIL

    def inorder_tree_walk(self, x):
        if x != self.NIL:
            self.inorder_tree_walk(x.left)
            print(x.key, end=" ")
            self.inorder_tree_walk(x.right)

    def tree_search(self, x, k):
        if x == self.NIL or k == x.key:
            return x
        if k < x.key:
            return self.tree_search(x.left, k)
        else:
            return self.tree_search(x.right, k)

    def iterative_tree_search(self, x, k):
        while x != self.NIL and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def tree_minimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    def tree_maximum(self, x):
        while x.right != self.NIL:
            x = x.right
        return x

    def tree_successor(self, x):
        if x.right != self.NIL:
            return self.tree_minimum(x.right)
        y = x.parent
        while y != self.NIL and x == y.right:
            x = y
            y = y.parent
        return y

    def tree_insert(self, z):
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

    def tree_delete(self, z):
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
        return y
    
class RedBlackTreeNode(TreeNode):
    def __init__(self, key):
        super().__init__(key)
        self.color = "RED"

class RedBlackTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
        self.NIL = RedBlackTreeNode(None)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    def left_rotate(self, x):
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

    def right_rotate(self, x):
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

    def rb_insert(self, z):
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

    def rb_insert_fixup(self, z):
        while z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "RED":
                    z.parent.color = "BLACK"  
                    y.color = "BLACK"          
                    z.parent.parent.color = "RED"  
                    z = z.parent.parent         
                else :
                    if z == z.parent.right:
                        z = z.parent              
                        self.left_rotate(z)       
                    z.parent.color = "BLACK"      
                    z.parent.parent.color = "RED" 
                    self.right_rotate(z.parent.parent)  
            else:
                y = z.parent.parent.left
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"         
                    z.parent.parent.color = "RED"
                    z = z.parent.parent         
                else:
                    if z == z.parent.left:
                        z = z.parent              
                        self.right_rotate(z)       
                    z.parent.color = "BLACK"      
                    z.parent.parent.color = "RED" 
                    self.left_rotate(z.parent.parent)  
        self.root.color = "BLACK"  

# 테스트
rbt = RedBlackTree()
keys_to_insert = [4, 1, 2, 3, 4]
for key in keys_to_insert:
    rbt.rb_insert(RedBlackTreeNode(key))

print("[초기 정렬]")
rbt.inorder_tree_walk(rbt.root)
print()
print()

# insert 195
rbt.tree_insert(TreeNode(195))
print("[insert 195]")
rbt.inorder_tree_walk(rbt.root)
print()
print()