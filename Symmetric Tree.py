class Solution:
    def isSymmetric_recr_1(self, root: TreeNode) -> bool:  # one-liner, less readible
        return (dfs:=lambda left,right:left==right==None or left!=None and right is not None and left.val==right.val and dfs(left.right,right.left) and dfs(left.left, right.right) ) (root.left,root.right)
    
    def isSymmetric_recr_0(self, root: TreeNode) -> bool:  # more readible
        def dfs(left,right):
            if left==right==None:
                return True
            elif left is None or right is None or left.val!=right.val:
                return False
            return dfs(left.right,right.left) and dfs(left.left, right.right) 
        return dfs(root.left,root.right)
    
    def isSymetric_iter_2(self,root):  # same idea, implement it iteratively
        from queue import SimpleQueue 
        q=SimpleQueue()
        q.put((root.left,root.right))
        while not q.empty():
            left,right=q.get()
            if left!=right:
                if left==None or right==None or left.val!=right.val:
                    return False
                else:
                    q.put((left.left,right.right))
                    q.put((left.right,right.left))
        return True
    
    # I tried to do an infix traversal  on the binary tree and write each node to a list, then determine whether the list is a palindrome. 
    # This approach does not work because it will return true for the following test case:
    # [1,2,2,2,null,2] , which can be fixed by passing a writeNone parameter to dfs to output None if a node has one None child (but not two)
    # it still failed after passed 195/196 test cases: [5,4,1,null,1,null,4,2,null,2,null] which I could think of no cure
    def isSymetric_recr_inorder_flatten_3(self,root): 
        flat=[]
        def dfs(root,writeNone):
            if not root:
                if writeNone:
                    flat.append(None)
                return 
            dfs(root.left,root.left!=root.right)
            flat.append(root.val)
            dfs(root.right,root.left!=root.right)
        dfs(root,True) 
        if not len(flat)%2: #must be mirrored around root, so total node number must be odd number
            return False
        print(flat)
        left,right=0,len(flat)-1 # check for palindrome
        while left<=right:
            if flat[left]!=flat[right]:
                return False
            left,right=left+1,right-1
        return True
        
        
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSymetric_iter_2(root)