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

# 테스트
bst = BinarySearchTree()
# 교재 노드값들 삽입
keys_to_insert = [56, 26, 200, 18, 28, 190, 213, 12, 24, 27]
for key in keys_to_insert:
    bst.tree_insert(TreeNode(key))

print("[초기 정렬]")
bst.inorder_tree_walk(bst.root)
print()
print()

# insert 195
bst.tree_insert(TreeNode(195))
print("[insert 195]")
bst.inorder_tree_walk(bst.root)
print()
print()

# delete 190
node_to_delete = bst.iterative_tree_search(bst.root, 190)
if node_to_delete != bst.NIL:
    bst.tree_delete(node_to_delete)
print("[delete 190]")
bst.inorder_tree_walk(bst.root)
print()
print()