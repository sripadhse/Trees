public class Solution {
    public TreeNode SortedArrayToBST(int[] nums) {
        
        if(nums == null || nums.Length == 0)
            return null;
        
        return buildBST(nums, 0, nums.Length - 1);
    }
    
    private TreeNode buildBST(int[] nums, int start, int end)
    {
        if(nums == null || nums.Length == 0 || start > end)
            return null;
        
        int mid = (end - start) / 2 + start;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = buildBST(nums, start, mid - 1);
        root.right = buildBST(nums, mid + 1, end);
        
        return root;
    }
}