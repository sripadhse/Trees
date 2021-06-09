class Solution {
    List<List<Integer>> res = new ArrayList<List<Integer>>();
    public List<List<Integer>> levelOrder(TreeNode root) {
        util(root , 0);
    return res;
    }
    
    public  void util(TreeNode root , int level){
        if(root == null)
            return;
        
        if(res.size() == level)
            res.add(new ArrayList<>());
         res.get(level).add(root.val);
        
        util(root.left , level + 1);
        util(root.right , level + 1);
    }
}
