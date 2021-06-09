class Solution:
    def isValidBST(self, root: TreeNode) -> bool:



        def helper(node, lower = float('-inf'), upper = float('inf')):
            if(not node):
                return True

            if(node.val<=lower or node.val>=upper):
                return False
            if not helper(node.right, node.val, upper):
                return False
            if not helper(node.left, lower, node.val):
                return False
            return True


        return helper(root)