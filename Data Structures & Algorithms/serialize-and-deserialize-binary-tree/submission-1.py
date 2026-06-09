# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #use bfs, use a queue, seperate node vals through #; null represented through _
        def bfs(queue):
            nonlocal res
            if not queue:
                return
            traversal = []
            for node in queue:
                if node:
                    res += str(node.val) + "#"
                    traversal.append(node.left)
                    traversal.append(node.right)
                else:
                    res += "_#"
            bfs(traversal)

        res = ""
        if not root:
            return res
        queue = [root]
        bfs(queue)
        return res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return
        arr = data.split("#")
        root = TreeNode(int(arr.pop(0)))
        
        def create(queue):
            if not queue:
                return
            traverse = []
            for node in queue:
                left = arr.pop(0)
                right = arr.pop(0)
                if left != "_":
                    temp = TreeNode(int(left))
                    node.left = temp
                    traverse.append(temp)
                if right != "_":
                    temp = TreeNode(int(right))
                    node.right = temp
                    traverse.append(temp)
            create(traverse) 

        queue = [root]
        create(queue)
        return root

            