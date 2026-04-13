# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def bfs(queue, data=""):
            if not queue:
                return data
            traverse = []
            for node in queue:
                if node:
                    data += str(node.val) + "_"
                    traverse.append(node.left)
                    traverse.append(node.right)
                else:
                    data += "#_"
            return bfs(traverse, data)

        return bfs([root])

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        curr = ""
        arr = []
        for i in range(len(data)):
            if data[i] == "_":
                arr.append(curr)
                curr = ""
            else:
                curr += data[i]

        val = arr.pop(0)
        if val == "#":
            return None

        root = TreeNode(int(val))
        queue = [root]       
        def create(queue):
            if not queue:
                return

            traverse = []
            for node in queue:
                left = arr.pop(0)
                right = arr.pop(0)
                if left != "#":
                    temp = TreeNode(int(left))
                    print(temp.val)
                    node.left = temp
                    traverse.append(temp)
                if right != "#":
                    temp = TreeNode(int(right))
                    node.right = temp
                    traverse.append(temp)
            create(traverse)
        create(queue)
        return root


        
