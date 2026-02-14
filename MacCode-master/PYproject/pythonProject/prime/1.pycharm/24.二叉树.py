from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"当前节点:{self.val},左子节点:{self.left.val if self.left else None},右子节点:{self.right.val if self.right else None}"


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.queue = []

    def insert_node(self, val):
        new_node = TreeNode(val)
        self.queue.append(new_node)
        self.val = new_node.val
        
        if self.root is None:
            self.root = new_node  # 根节点为空, 则新节点为根节点
        else:
            if self.queue[0].left is None:  # 左子节点为空, 则新节点为左子节点
                self.queue[0].left = new_node
            else:  # 右子节点为空, 则新节点为右子节点
                self.queue[0].right = new_node
                self.queue.pop(0)

    def pre_order(self,current_node:TreeNode):
        #先序遍历
        if current_node is None:
            return
        else:
            print(current_node.val,end=" ")
            if current_node.left:
                self.pre_order(current_node.left)
            if current_node.right:
                self.pre_order(current_node.right)
                
    def mid_order(self,current_node:TreeNode):
        #中序遍历
        if current_node :
            if current_node.left:
                self.pre_order(current_node.left)
            print(current_node.val,end=" ")
            if current_node.right:
                self.pre_order(current_node.right)

    def last_order(self,current_node:TreeNode):
        #序遍历
        if current_node :
            if current_node.left:
                self.pre_order(current_node.left)
            if current_node.right:
                self.pre_order(current_node.right)
            print(current_node.val,end=" ")
    
    def level_order(self):
        queue=deque()#双端队列
        queue.append(self.root)
        while queue:
            node:TreeNode=queue.popleft()
            print(node.val,end=" ")
            #依次加入队列右侧
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        

if __name__ == "__main__":
    tree = Tree()
    for i in range(1,10):
        tree.insert_node(i)
    
    tree.pre_order(tree.root)
    
    print()
    tree.mid_order(tree.root)
    print()
    tree.last_order(tree.root)
    print()
    tree.level_order()