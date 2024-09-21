import unittest
from binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insertion(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(2)
        self.bst.insert(4)
        self.assertEqual(self.bst.search(5).data, 5)
        self.assertEqual(self.bst.search(3).data, 3)
        self.assertEqual(self.bst.search(7).data, 7)
        self.assertEqual(self.bst.search(2).data, 2)
        self.assertEqual(self.bst.search(4).data, 4)

    def test_deletion(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(2)
        self.bst.insert(4)
        self.bst.delete(5)
        self.assertIsNone(self.bst.search(5))
        self.bst.delete(3)
        self.assertIsNone(self.bst.search(3))

    def test_traversal(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(2)
        self.bst.insert(4)
        inorder_traversal = [2, 3, 4, 5, 7]
        preorder_traversal = [5, 3, 2, 4, 7]
        postorder_traversal = [2, 4, 3, 7, 5]
        self.assertEqual(list(self.bst.inorder_traversal()), inorder_traversal)
        self.assertEqual(list(self.bst.preorder_traversal()), preorder_traversal)
        self.assertEqual(list(self.bst.postorder_traversal()), postorder_traversal)

    def test_empty_tree(self):
        self.assertIsNone(self.bst.search(10))
        # No need to convert to list, call the traversal methods directly
        self.bst.inorder_traversal()
        self.bst.preorder_traversal()
        self.bst.postorder_traversal()

if __name__ == '__main__':
    unittest.main()