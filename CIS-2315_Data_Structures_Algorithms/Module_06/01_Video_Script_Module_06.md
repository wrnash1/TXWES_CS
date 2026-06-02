# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 06 — AVL Trees & Red-Black Trees

**Estimated Duration:** 22–26 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Python terminal for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - This module is conceptually heavier than Module 05. The goal is not to have students implement a full Red-Black tree from scratch — that is a multi-week topic. The goal is: understand why self-balancing trees exist, what rotations do, and what the height guarantee means.
> - Draw every rotation on the board before writing code. Students who can draw a rotation have understood it.
> - AVL balance factor: height(right) - height(left). Values -1, 0, +1 are balanced. Outside triggers rotation.
> - Red-Black properties (5 rules) are the most testable content in this module. State them clearly.
> - Interview context: Red-Black trees are behind Python `sortedcontainers`, Java `TreeMap`, C++ `std::map`. Students must know this connection.
> - Common mistakes: confusing which rotation (LL/LR/RL/RR), forgetting to update heights after rotation.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 06 | AVL Trees & Red-Black Trees | CIS-2315"]**

"Module 05 showed that BST operations are O(log n) average case but O(n) worst case when the tree is skewed. This module introduces self-balancing trees that maintain O(log n) height after every insertion and deletion — guaranteeing O(log n) in the worst case. We cover two families: AVL trees, which enforce strict balance using rotations, and Red-Black trees, which use a color-based relaxed condition. Both power the sorted collections in every major programming language."

---

## [01:30 – 07:00] Part 1 — The Balance Problem and AVL Trees

**[SHOW SLIDE: "BST Degeneration"]**

"Inserting values in sorted order produces a chain:

```text
Insert 1, 2, 3, 4, 5:
1
 \
  2
   \
    3
     \
      4
       \
        5
Height = 4. Search is O(n).
```

The fix: maintain a balance condition and restore it after every mutation.

[PAUSE]

**AVL Trees** (Adelson-Velsky and Landis, 1962) maintain: for every node, the heights of its left and right subtrees differ by at most 1.

Define the balance factor as `height(right) - height(left)`:

- -1, 0, +1: balanced — no action needed
- -2 or +2: unbalanced — apply a rotation to restore balance

An AVL tree of height h contains at least the h-th Fibonacci number of nodes, so h = O(log n) is guaranteed.

[PAUSE]

We need one piece of bookkeeping: each node stores its height.

```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1   # new leaf has height 1

def height(node):
    return node.height if node else 0

def get_balance(node):
    return height(node.right) - height(node.left) if node else 0
```

After every insert, we update heights bottom-up and check the balance factor."

---

## [07:00 – 13:00] Part 2 — AVL Rotations

**[SHOW SLIDE: "Four Rotation Cases"]**

"When balance factor is +2 or -2, we apply a rotation. There are four cases.

**[SHOW DIAGRAM: LL — right rotation]**

Case LL: left-heavy (balance -2), imbalance is in left-left direction. Fix: right rotation.

```text
      z                 y
     /                 / \
    y        →        x   z
   /
  x
```

```python
def right_rotate(z):
    y = z.left
    T3 = y.right       # y's right subtree → z's new left

    y.right = z
    z.left = T3

    # Update heights bottom-up: z is now below y
    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y            # y is the new subtree root
```

[PAUSE]

**[SHOW DIAGRAM: RR — left rotation]**

Case RR: right-heavy (balance +2), imbalance in right-right direction. Fix: left rotation (mirror of LL).

```python
def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y
```

[PAUSE]

**[SHOW DIAGRAM: LR — double rotation (left then right)]**

Case LR: left-heavy, but imbalance is in left-right direction.

```text
    z               z              y
   /               /              / \
  x      →        y      →       x   z
   \              /
    y             x
```

Fix: left rotate the left child, then right rotate the root.

```python
# In avl_insert: balance < -1 and key > root.left.key → LR case
root.left = left_rotate(root.left)
return right_rotate(root)
```

[PAUSE]

**[SHOW DIAGRAM: RL — double rotation (right then left)]**

Case RL: right-heavy, imbalance in right-left direction. Fix: right rotate the right child, then left rotate the root.

```python
# In avl_insert: balance > 1 and key < root.right.key → RL case
root.right = right_rotate(root.right)
return left_rotate(root)
```

The memory aid: the case name (LL, LR, RL, RR) describes the path to the inserted node. LL means left-left (left child's left subtree), and the fix is the opposite single rotation. LR means left-right (left child's right subtree), and the fix is a double rotation in the opposite direction."

---

## [13:00 – 17:30] Part 3 — Complete AVL Insert

**[SHOW SLIDE: "AVL Insert Function"]**

"Now the full insert ties everything together:

```python
def avl_insert(root, key):
    # Step 1: Standard BST insert
    if not root:
        return AVLNode(key)
    if key < root.key:
        root.left = avl_insert(root.left, key)
    elif key > root.key:
        root.right = avl_insert(root.right, key)
    else:
        return root  # duplicate ignored

    # Step 2: Update this node's height
    root.height = 1 + max(height(root.left), height(root.right))

    # Step 3: Check balance and apply rotation if needed
    balance = get_balance(root)

    if balance < -1 and key < root.left.key:    # LL
        return right_rotate(root)
    if balance > 1 and key > root.right.key:     # RR
        return left_rotate(root)
    if balance < -1 and key > root.left.key:     # LR
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance > 1 and key < root.right.key:     # RL
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root
```

**[DEMO — Insert [1, 2, 3] and watch the rotation fire]**

```python
root = None
for k in [1, 2, 3]:
    root = avl_insert(root, k)

# Without AVL: 1→2→3 chain, height 3
# With AVL: after inserting 3, RR case fires, left rotation gives:
#    2
#   / \
#  1   3
# Height = 2, balanced
```

The tree self-heals. Insert sorted data and the AVL tree stays balanced at every step."

---

## [17:30 – 21:00] Part 4 — Red-Black Trees

**[SHOW SLIDE: "Red-Black Tree — Five Properties"]**

"Red-Black trees use a color attribute — red or black — on each node, with five rules that guarantee O(log n) height.

**The five Red-Black properties:**

1. Every node is red or black.
2. The root is black.
3. Every NIL leaf is black. (NIL sentinels mark the absence of a real child.)
4. If a node is red, both children are black. (No two consecutive red nodes on any path.)
5. Every path from any node to its descendant NIL leaves has the same number of black nodes (the black-height of that node).

[PAUSE]

**[SHOW DIAGRAM: valid Red-Black tree]**

Why does this guarantee O(log n) height? Property 5 ensures equal black-height across all paths. Property 4 ensures no path can have two consecutive red nodes. Therefore the longest possible path alternates red-black-red-black... The longest path is at most 2× the shortest, and the shortest has black-height bh. Since the tree has at least 2^bh - 1 nodes, bh = O(log n), so height ≤ 2bh = O(log n).

[PAUSE]

**Red-Black vs AVL:**

AVL is stricter — height difference at most 1 everywhere. Red-Black is looser — the 2× path length guarantee. The trade-off: AVL has slightly faster lookups (shorter tree), Red-Black has faster inserts and deletes (fewer rotations — at most 3 for insert or delete in Red-Black vs potentially O(log n) for AVL delete).

Production systems that do many inserts and deletes choose Red-Black. Read-heavy systems with rare mutations may prefer AVL."

---

## [21:00 – 24:00] Part 5 — Complexity Summary and Closing

**[SHOW SLIDE: "Self-Balancing Tree Complexity"]**

"| Operation | Plain BST (worst) | AVL | Red-Black |
|---|---|---|---|
| Search | O(n) | O(log n) | O(log n) |
| Insert | O(n) | O(log n) | O(log n) |
| Delete | O(n) | O(log n) | O(log n) |
| Rotations per insert | 0 | ≤ 2 | ≤ 2 |
| Rotations per delete | 0 | O(log n) | ≤ 3 |

All operations are O(log n) guaranteed for both self-balancing variants.

[PAUSE]

**What to know for interviews:**

1. Self-balancing trees fix the O(n) worst case of plain BSTs.
2. AVL uses balance factor ±1 with four rotation cases: LL, RR, LR, RL.
3. Red-Black uses five color properties with O(log n) height guaranteed.
4. Python `sortedcontainers.SortedList`, Java `TreeMap`, C++ `std::map` — all Red-Black under the hood.
5. When an interviewer asks for O(log n) sorted insertions and range queries, the answer is a self-balancing BST.

The lab has you implement a complete AVL tree. The quiz tests rotations, balance factors, and Red-Black properties. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 06 — AVL Trees & Red-Black Trees]**

---

## Additional Resources

- [VisuAlgo — AVL Tree and Red-Black Tree](https://visualgo.net/en/bst)
- [NeetCode — Self-Balancing BSTs](https://www.youtube.com/watch?v=q4fnJZr8ztY)
- [Wikipedia — Red-Black Tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)
- [Python sortedcontainers](http://www.grantjenks.com/docs/sortedcontainers/)
