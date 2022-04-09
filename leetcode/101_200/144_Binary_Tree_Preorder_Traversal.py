"""
144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        data = []

        def preorder(root, data):
            if root:
                data.append(root.val)
                preorder(root.left, data)
                preorder(root.right, data)

        preorder(root, data)
        return data


root = [1, null, 2, 3]
root = []
root = [1]
obj = Solution()
result = obj.preorderTraversal(root)
print(result)

"""
Time and Memory Calculation
"""
time_elapsed = (time.perf_counter() - time_start)
memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024
print("Time  : %5.5f secs \nMemory: %5.5f KByte" % (time_elapsed, memMb))
