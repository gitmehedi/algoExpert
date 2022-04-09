"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
import resource
import time
from typing import Optional, List

time_start = time.perf_counter()


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        data = []

        def inorder(root, data):
            if root:
                inorder(root.left, data)
                data.append(root.val)
                inorder(root.right, data)

        inorder(root, data)

        return data


root = [1, null, 2, 3]
root = []
root = [1]
obj = Solution()
result = obj.inorderTraversal(root  )
print(result)

"""
Time and Memory Calculation
"""
time_elapsed = (time.perf_counter() - time_start)
memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024
print("Time  : %5.5f secs \nMemory: %5.5f KByte" % (time_elapsed, memMb))
