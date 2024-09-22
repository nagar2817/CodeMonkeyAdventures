**1. Find a value in a Binary Search Tree:**

- **Problem:** [Find a Value in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)
- **Solution:**
  ```python
   class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return root
  ```

**2. Insertion of a node in a Binary Search Tree:**

- **Problem:** [Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
- **Solution:**
  ```python
  def insertIntoBST(root, val):
      if not root:
          return TreeNode(val)

      if val < root.val:
          root.left = insertIntoBST(root.left, val)
      else:
          root.right = insertIntoBST(root.right, val)

      return root
  ```

**3. Deletion of a node in Binary Search Tree:**

- **Problem:** [Delete Node in a Binary Search Tree](https://leetcode.com/problems/delete-node-in-a-bst/)
- **Solution:**
  ```python
    class Solution:
        def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
            if not root:
            return None

            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            elif key > root.val:
                root.right = self.deleteNode(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    temp = self._find_min(root.right)
                    root.val = temp.val
                    root.right = self.deleteNode(root.right,temp.val)
            return root

        def _find_min(self,node):
            while node.left:
                node = node.left
            return node
            
  ```

**4. Find minimum value in a Binary Search Tree:**

- **Problem:** Minimum Value in a Binary Search Tree []
- **Solution:**
  ```python
  def minValueBST(root):
      while root.left:
          root = root.left

      return root.val
  ```

**5. Find maximum value in a Binary Search Tree:**

- **Problem:** Maximum Value in a Binary Search Tree [invalid URL removed]
- **Solution:**
  ```python
  def maxValueBST(root):
      while root.right:
          root = root.right

      return root.val
  ```

**6. Find inorder successor in a Binary Search Tree:**

- **Problem:** [Inorder Successor in Binary Search Tree](https://leetcode.com/problems/inorder-successor-in-bst-ii/)
- **Solution:**
```python
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        if p.right:
            # If the node has a right child, the successor is the leftmost node in the right subtree
            successor = p.right
            while successor.left:
                successor = successor.left
            return successor

        successor = None
        current = root
        while current:
            if p.val < current.val:
                successor = current
                current = current.left
            else:
                current = current.right

        return successor
  ```

**7. Find inorder predecessor in a Binary Search Tree:**

- **Problem:** Inorder Predecessor in Binary Search Tree
- **Solution:**
```python
class Solution:
    def inorderPredecessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        if not root:
            return None

        if p.val < root.val:
            return self.inorderPredecessor(root.left, p)

        # If p is in the right subtree, the predecessor is either in the right subtree or the current node
        successor = self.inorderPredecessor(root.right, p)
        if successor:
            return successor

        return roott
  ```

**8. Check if a binary tree is a BST or not:**

- **Problem:** [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- **Solution:**
  ```python
  def isValidBST(root):
      def helper(node, min_val, max_val):
          if not node:
              return True

          if node.val <= min_val or node.val >= max_val:
              return False

          return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)

      return helper(root, float('-inf'), float('inf'))
  ```

**9. LCA of 2 nodes in a BST:**

- **Problem:** [Lowest Common Ancestor of Two Nodes in a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)
- **Solution:**
  ```python
  def lowestCommonAncestorBST(root, p, q):
      while root:
          if p.val < root.val and q.val < root.val:
              root = root.left
          elif p.val > root.val and q.val > root.val:
              root = root.right
          else:
              return root

      return None
  ```

**10. Kth smallest element in a BST:**

- **Problem:** [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- **Solution:**
  ```python
  def kthSmallest(root, k):
      stack = []

      while root or stack:
          while root:
              stack.append(root)
              root = root.left

          root = stack.pop()
          k -= 1
          if k == 0:
              return root.val

          root = root.right

      return -1
  ```

**11. Kth largest element in a BST:**

- **Problem:** Kth Largest Element in a BST []
- **Solution:**
  ```python
  def kthLargest(root, k):
      """
      :type root: TreeNode
      :type k: int
      :rtype: int
      """

      stack = []

      while root or stack:
          while root:
              stack.append(root)
              root = root.right

          root = stack.pop()
          k -= 1
          if k == 0:
              return root.val

          root = root.left

      return -1
  ```

## 13. Count Complete Tree Nodes:

**Problem:** [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)

**Solution:**

```python
def countCompleteTreeNodes(root):
    if not root:
        return 0

    left_height = right_height = 0

    temp = root
    while temp:
        left_height += 1
        temp = temp.left

    temp = root
    while temp:
        right_height += 1
        temp = temp.right

    if left_height == right_height:
        return 2 ** left_height - 1

    return 1 + countCompleteTreeNodes(root.left) + countCompleteTreeNodes(root.right)
```

## 14. Find the median of BST:

**Problem:** Find the Median of a BST [invalid URL removed]

**Solution:**

```python
def findMedian(root):
    def inorder(root, values):
        if not root:
            return

        inorder(root.left, values)
        values.append(root.val)
        inorder(root.right, values)

    values = []
    inorder(root, values)

    n = len(values)
    if n % 2 == 0:
        return (values[n // 2 - 1] + values[n // 2]) / 2
    else:
        return values[n // 2]
```

## 15. Count BST nodes that lie in a given range:

**Problem:** Count BST Nodes That Lie in a Given Range []

**Solution:**

```python
def countRange(root, low, high):
    """
    :type root: TreeNode
    :type low: int
    :type high: int
    :rtype: int
    """

    if not root:
        return 0

    if root.val < low:
        return countRange(root.right, low, high)
    elif root.val > high:
        return countRange(root.left, low, high)
    else:
        return 1 + countRange(root.left, low, high) + countRange(root.right, low, high)
```

## 16. Largest BST in a binary tree:

**Problem:** Largest BST Subtree [invalid URL removed]

**Solution:**

```python
def largestBSTSubtree(root):
    class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return (True, float('inf'), float('-inf'), 0)  # Valid subtree with min/max values and size

            left_is_bst, left_min, left_max, left_size = helper(node.left)
            right_is_bst, right_min, right_max, right_size = helper(node.right)

            if not left_is_bst or not right_is_bst or left_max >= node.val or right_min <= node.val:
                return (False, 0, 0, 0)  # Not a BST

            # Calculate min, max, and size for the current subtree
            curr_min = min(left_min, node.val)
            curr_max = max(right_max, node.val)
            curr_size = left_size + right_size + 1

            return (True, curr_min, curr_max, curr_size)

        _, _, _, max_size = helper(root)
        return max_size
```

## 17. Flatten BST to sorted linked list:

**Problem:** Flatten a Binary Search Tree to a Linked List [https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/)

**Solution:**

```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        right_subtree = root.right
        root.right = root.left
        root.left = None
        self.flatten(right_subtree)
        curr = root
        while curr.right:
            curr = curr.right
        curr.right = right_subtree

```

## 18. Construct BST from preorder traversal:

**Problem:** Construct Binary Search Tree from Preorder Traversal [https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)

**Solution:**

```python
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = [0]
        def helper(A,bound):
            if i[0] == len(A) or A[i[0]] > bound:
                return None
            root = TreeNode(A[i[0]])
            i[0] +=1
            root.left = helper(A,root.val)
            root.right = helper(A,bound)
            return root
        return helper(preorder, float('inf'))
            
```

## 19. Convert BST into balanced BST:

**Problem:** Convert a Binary Search Tree to a Balanced Binary Search Tree [https://leetcode.com/problems/balance-a-binary-search-tree/submissions/1398127416/](https://leetcode.com/problems/balance-a-binary-search-tree/submissions/1398127416/)

**Solution:**

```python
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # Flatten the BST into a sorted list
        def inorder(node, result):
            if not node:
                return
            inorder(node.left, result)
            result.append(node.val)
            inorder(node.right, result)

        result = []
        inorder(root, result)

        # Construct a balanced BST from the sorted list
        def constructBST(values, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(values[mid])
            node.left = constructBST(values, start, mid - 1)
            node.right = constructBST(values, mid + 1, end)
            return node

        return constructBST(result, 0, len(result) - 1)
```

## 20. Merge two BSTs:

**Problem:** Merge Two Binary Search Trees

**Solution:**

```python
def merge(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1

    # Choose the root of the merged tree based on the values
    if root1.val < root2.val:
        merged_root = root1
        merged_root.right = self.merge(root1.right, root2)
    else:
        merged_root = root2
        merged_root.left = self.merge(root1, root2.left)

    return merged_root
```
