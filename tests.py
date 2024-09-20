import unittest
from Linked_List import LinkedList, Node

class LinkedListTest(unittest.TestCase):
    def test_append(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.head.next.data, 2)
        self.assertEqual(linked_list.head.next.next.data, 3)

    def test_insert(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.insert(1, 2)
        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.head.next.data, 2)
        self.assertEqual(linked_list.head.next.next.data, 3)

    def test_delete(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.delete(1)
        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.head.next.data, 3)

    def test_search(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertTrue(linked_list.search(2))
        self.assertFalse(linked_list.search(4))

    def test_reverse(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.reverse()
        self.assertEqual(linked_list.head.data, 3)
        self.assertEqual(linked_list.head.next.data, 2)
        self.assertEqual(linked_list.head.next.next.data, 1)

if __name__ == '__main__':
    unittest.main() 