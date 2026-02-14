struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    int dfs(TreeNode *root, int presum)
    {
        presum = presum * 10 + root->val;
        if (root->left == nullptr && root->right == nullptr)
            return presum;
        int ret = 0;
        if (root->left)
            ret += dfs(root->left, presum);
        if (root->right)
            ret += dfs(root->right, presum);
        return ret;
    }

    int sumNumbers(TreeNode *root)
    {
        // 先序遍历
        return dfs(root, 0);
    }
};