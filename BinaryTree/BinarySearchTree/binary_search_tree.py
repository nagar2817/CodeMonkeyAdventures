class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.Insert_Recursive(self.root,data)
    def Insert_Recursive(self,root,data):
        if data < root.data:
            if not root.left:
                root.left = Node(data)
            else:
                self.Insert_Recursive(root.left,data)
        else:
            if not root.right:
                root.right = Node(data)
            else:
                self.Insert_Recursive(root.right,data)
    
    def search(self,data):
        return self.Search_Recursive(self.root,data)
    def Search_Recursive(self,node,data):
        if node is None or node.data == data:
            return node 
        if node.data < data:
            return self.Search_Recursive(node.right,data)
        else:
            return self.Search_Recursive(node.left,data)
    
    def delete(self,data):
        self.root =  self.Delete_Recursive(self.root,data)
    def Delete_Recursive(self,node,data):
        if node is None:
            return node 
        if node.data < data:
            node.right = self.Delete_Recursive(node.right,data)
        elif node.data > data:
            node.left =  self.Delete_Recursive(node.left,data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._find_min(node.right)
                node.data = temp.data
                node.right = self.Delete_Recursive(node.right,temp.data)
        return node
    def _find_min(self,node):
        while node.left:
            node = node.left
        return node
    
    def inorder_traversal(self):
        if self.root:
            self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node):
        if node:
            self._inorder_traversal_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_traversal_recursive(node.right)

    def preorder_traversal(self):
        if self.root:
            self._preorder_traversal_recursive(self.root)

    def _preorder_traversal_recursive(self, node):
        if node:
            print(node.data, end=" ")
            self._preorder_traversal_recursive(node.left)
            self._preorder_traversal_recursive(node.right)

    def postorder_traversal(self):
        if self.root:
            self._postorder_traversal_recursive(self.root)

    def _postorder_traversal_recursive(self, node):
        if node:
            self._postorder_traversal_recursive(node.left)
            self._postorder_traversal_recursive(node.right)
            print(node.data,end=" ")