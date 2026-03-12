# Define the TreeNode class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value  
        self.left = left   
        self.right = right  
# Function to gather information about the binary tree
def tree_info(node):
    """
    Prints height, number of leaf nodes, whether the tree is full, 
    and whether the tree is balanced.
    """
    
    # Helper function to compute height of tree
    def height(n):
        if n is None:
            return -1  
        return 1 + max(height(n.left), height(n.right))

    # Helper function to count leaf nodes
    def count_leaves(n):
        if n is None:
            return 0
        if n.left is None and n.right is None:
            return 1  
        return count_leaves(n.left) + count_leaves(n.right)

    # Helper function to check if tree is full
    def is_full(n):
        if n is None:
            return True  # Empty tree is considered full
        if (n.left is None) != (n.right is None):
            return False  # One child only, not full
        return is_full(n.left) and is_full(n.right)

    # Helper function to check if tree is balanced
    def is_balanced(n):
        if n is None:
            return True, -1  
        left_balanced, left_height = is_balanced(n.left)
        right_balanced, right_height = is_balanced(n.right)
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return balanced, 1 + max(left_height, right_height)

    # Compute required info
    tree_height = height(node)
    leaf_count = count_leaves(node)
    full = "Yes" if is_full(node) else "No"
    balanced, _ = is_balanced(node)
    balanced = "Yes" if balanced else "No"

   
    print(f"Height of the tree: {tree_height}")
    print(f"Number of leaf nodes: {leaf_count}")
    print(f"Is Full: {full}")
    print(f"Is Balanced: {balanced}")


if __name__ == "__main__":
    # Construct the tree
    #       3
    #     /   \
    #    9     8
    #   / \
    #  4   5
    root = TreeNode(1, 
                    TreeNode(2, TreeNode(4), TreeNode(5)), 
                    TreeNode(3))

    tree_info(root)
