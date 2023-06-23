Data Structure and Algorithms
----------------------------------

- [Data Structure and Algorithms](#data-structure-and-algorithms)
- [Algorithms](#algorithms)
    - [Tree Algorithms](#tree-algorithms)
        - [References](#references)

## Algorithms

A data structure is a way of organizing, storing, and managing data to be used efficiently. Data structures are an
important part of several computer algorithms and programs.

Types of Algorithms are listed below.

### Tree Algorithms

A tree data structure is a collection of nodes connected by edges. Each node contains a value or data which may or may
not have a child node.

Tree Data Structure Terminology

 Terminology    | Description                                                                                                                                                 | Logic | Examples 
 ----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|----------
 Node           | Each vertex of the tree is node                                                                                                                             | Logic | Examples 
 Tree           | Topmost node of a tree.                                                                                                                                     | Logic | Examples 
 Parent Node    | The node has an edge-sharing to a child node.                                                                                                               | Logic | Examples 
 Child Node     | The sub-node of a parent node is the child node.                                                                                                            | Logic | Examples 
 Leaf Node      | The last node which does have any subnode is the leaf node.                                                                                                 | Logic | Examples 
 Edge           | Connecting link between two nodes.                                                                                                                          | Logic | Examples 
 Sibling        | Nodes with the same parent are siblings.                                                                                                                    | Logic | Examples 
 Height         | The height of a tree is the length of the longest path from the root to a leaf node. It is calculated with the total number of edges.                       | Logic | Examples 
 Depth          | The number of edges from the root node to that node is called the Depth of that node.    Depth of a tree = Height of tree – 1                               | Logic | Examples 
 Level          | Each step from top to bottom is called a Level. If the root node is at level 0, its next child node is at level 1, its grandchild is at level 2, and so on. | Logic | Examples 
 Sub-Tree       | Descendants of a node represent a subtree.                                                                                                                  | Logic | Examples 
 Degree of Node | The degree of a node represents the total number of children in it.                                                                                         | Logic | Examples 

#### Types of Tree Data Structure
The following are the different types of trees data structures:
- Binary Tree 
- Binary Search Tree (BST)
- AVL Tree 
- B-Tree 

##### Binary Tree
A binary tree is a tree data structure in which each node can have 0, 1, or 2 children – left and right child.

**Properties**   
- The maximum number of nodes at any level ‘L’ in a binary tree is 2
- The minimum number of nodes in a binary tree of height H is H + 1
- The maximum number of nodes in a binary tree of height H is 2H+1 – 1
- Total Number of leaf nodes in a Binary Tree = Total Number of nodes with two children + 1
- The maximum number of nodes at each level of i is 2i.
- Searching operation takes O(log2N)  

**Categories**
- **Perfect binary tree**: Every internal node has two child nodes. All the leaf nodes are at the same level.
- **Full binary tree**: Every parent node or an internal node has either exactly two children or no child nodes.
- **Complete binary tree**: All levels except the last one are full of nodes.
- **Degenerate binary tree**: All the internal nodes have only one child.
- **Balanced binary tree**: The left and right trees differ by either 0 or 1.

**Applications**
- Decision Tree – Machine learning Algorithm
- Working with Morse Code
- Binary Expression Trees

##### Binary Search Tree (BST)
A binary search tree (BST) is also called an ordered or sorted binary tree in which the value at the left sub-tree is lesser than that of the root and the right subtree has a value greater than that of the root.

Every binary search tree is a binary tree. 

**Properties**
- Each node has a maximum of up to two children.
- The value of all the nodes in the left sub-tree is less than the value of the root.
- The value of all the nodes in the right subtree is greater than or equal to the value of the root.
- This rule is recursively valid for all the left and right subtrees of the root.

**Applications**
- Used to efficiently store data in the sorted form to quickly access and search stored elements.
- Given ‘A’ a sorted array, determine how many times x occurs in ‘A’.
- Player ‘A’ chooses a secret number ‘n’. Player ‘B’ can guess a number x and A replies how x
- compares to n (equal, larger, smaller). What’s an efficient strategy for B to guess ‘n’?

##### AVL Tree
AVL trees are a special kind of self-balancing binary search tree where the height of every node’s left and right subtree differs by at most one.

**Properties**
- The heights of the two child subtrees of any node differ by at most one.
- Balance Factor = (Height of Left Subtree – Height of Right Subtree).
- -1 Balance factor represents that the right subtree is one level higher than the left.
- 0 Balance factor represents that the height of the left subtree is equal to that of the right subtree.
- 1 Balance factor means that the left subtree is one level higher than the right subtree.
- The maximum possible number of nodes in the AVL tree of height H is 2H+1 – 1
- The minimum number of nodes in the AVL Tree of height H is given by a recursive relation: N(H) = N(H-1) + N(H-2) + 1
- Minimum possible height of AVL Tree using N nodes = ⌊log2N⌋ i.e floor value of log 2N
- The maximum height of the AVL Tree using N nodes is calculated using recursive relation: N(H) = N(H-1) + N(H-2) + 1

**Applications**
- In-memory sorts of sets and dictionaries
- Database applications that require frequent lookups for data

##### B-Tree
B tree is a self-balancing search tree wherein each node can contain more than one key and more than two children. It is a special type of m-way tree and a generalized binary search tree. B-tree can store many keys in a single node and can have multiple child nodes. This reduces the height and enables faster disk access.
 
**Properties**
- Every node contains at most m children.
- Every node contains at least m/2 children (except the root node and the leaf node).
- The root nodes should have a minimum of 2 nodes.
- All leaf nodes should be at the same level.

**Applications**
- Databases and file systems
- Multilevel indexing
- For quick access to the actual data stored on the disks
- To store blocks of data


#### References

- https://www.shiksha.com/online-courses/articles/tree-data-structures-types-properties-and-applications/
- 












