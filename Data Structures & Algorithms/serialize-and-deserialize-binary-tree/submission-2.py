# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = ""
        if not root:
            return s
        def bfs(arr):
            nonlocal s
            if not arr:
                return
            traverse = []
            for node in arr:
                if node:
                    traverse.append(node.left)
                    traverse.append(node.right)
                    s += str(node.val) + "_"
                else:
                    s += "#_"
            bfs(traverse)

        bfs([root])
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return
        queue = deque()
        curr = ""
        for s in data:
            if s == "_":
                queue.append(curr)
                curr = ""
            else:
                curr += s

        def makenode(val):
            if val == "#":
                return None
            return TreeNode(int(val))

        nodes = [makenode(queue.popleft())]
        root = nodes[0]
        while queue:
            traverse = []
            for node in nodes:
                if node:
                    node.left = makenode(queue.popleft())
                    node.right = makenode(queue.popleft())
                    traverse.append(node.left)
                    traverse.append(node.right)
            nodes = traverse.copy()


        return root


