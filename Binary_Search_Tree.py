class Binary_Search_Tree:
    # TODO.I have provided the public method skeletons. You will need
    # to add private methods to support the recursive algorithms
    # discussed in class

    class __BST_Node:
        # TODO The Node class is private. You may add any attributes and
        # methods you need. Recall that attributes in an inner class
        # must be public to be reachable from the the methods.

        def __init__(self, value):
            self.value = value
            self.height = 1
            self.left = None
            self.right = None

    def __init__(self):
        self.__root = None

    def insert_element(self, value):
        # Insert the value specified into the tree at the correct
        # location based on "less is left; greater is right" binary
        # search tree ordering. If the value is already contained in
        # the tree, raise a ValueError. Your solution must be recursive.
        # This will involve the introduction of additional private
        # methods to support the recursion control variable.
        self.__root = self.__rins(value, self.__root)
        return self.__root

    def __rins(self, value, curNode):
        if curNode is None:
            return Binary_Search_Tree.__BST_Node(value)
        else:
            if value > curNode.value:
                curNode.right = self.__rins(value, curNode.right)
                # update the height of the tree
                if curNode.right is None:
                    curNode.height = curNode.left.height + 1
                elif curNode.left is None:
                    curNode.height = curNode.right.height + 1
                else:
                    curNode.height = max(curNode.left.height, curNode.right.height) + 1
            elif value < curNode.value:
                curNode.left = self.__rins(value, curNode.left)
                # update the height of the tree
                if curNode.right is None:
                    curNode.height = curNode.left.height + 1
                elif curNode.left is None:
                    curNode.height = curNode.right.height + 1
                else:
                    curNode.height = max(curNode.left.height, curNode.right.height) + 1
            elif value == curNode.value:
                raise ValueError
        return self.__balance(curNode)

    def remove_element(self, value):
        # Remove the value specified from the tree, raising a ValueError
        # if the value isn't found. When a replacement value is necessary,
        # select the minimum value to the from the right as this element's
        # replacement. Take note of when to move a node reference and when
        # to replace the value in a node instead. It is not necessary to
        # return the value (though it would reasonable to do so in some
        # implementations). Your solution must be recursive.
        # This will involve the introduction of additional private
        # methods to support the recursion control variable.
        self.__root = self.__rrem(value, self.__root)
        return self.__root

    def __rrem(self, value, curNode):
        if curNode is None:
            raise ValueError
        if value == curNode.value:
            # when the node being removed has only the right child
            if curNode.left is None:
                temp = curNode.right
                return temp
            # when the node being removed has only the left child
            elif curNode.right is None:
                temp = curNode.left
                return temp
            # when the node being removed has both children
            else:
                temp = self.__find_min(curNode.right)
                curNode.value = temp.value
                curNode.right = self.__rrem(temp.value, curNode.right)
                # update the height of the tree
                if curNode.left is None:
                    curNode.height = curNode.right.height + 1
                elif curNode.right is None:
                    curNode.height = curNode.left.height + 1
                else:
                    curNode.height = max(curNode.left.height, curNode.right.height) + 1
                return self.__balance(curNode)
        else:
            if value > curNode.value:
                curNode.right = self.__rrem(value, curNode.right)
                # update the height of the tree
                if (curNode.right is None) and (curNode.left is None):
                    curNode.height = curNode.height - 1
                elif curNode.right is None:
                    curNode.height = curNode.left.height + 1
                elif curNode.left is None:
                    curNode.height = curNode.right.height + 1
                else:
                    curNode.height = max(curNode.left.height, curNode.right.height) + 1
            elif value < curNode.value:
                curNode.left = self.__rrem(value, curNode.left)
                # update the height of the tree
                if curNode.left is None and curNode.right is None:
                    curNode.height = curNode.height - 1
                elif curNode.left is None:
                    curNode.height = curNode.right.height + 1
                elif curNode.right is None:
                    curNode.height = curNode.left.height + 1
                else:
                    curNode.height = max(curNode.left.height, curNode.right.height) + 1
        return self.__balance(curNode)

    def __find_min(self, curNode):
        if curNode.left is None:
            return curNode
        else:
            return self.__find_min(curNode.left)

    def __findBalance(self, t):
        if t.left is None and t.right is None:
            balance = 0
        elif t.left is None:
            balance = t.right.height
        elif t.right is None:
            balance = (-1) * t.left.height
        else:
            balance = t.right.height - t.left.height
        return balance

    def __balance(self, t):
        balance = self.__findBalance(t)
        # when the tree is balanced
        if abs(balance) <= 1:
            return t
        # when right side is heavier
        elif balance > 1:
            if t.right.left is None:
                return self.__leftRotate(t)
            elif t.right.right is None:
                t.right = self.__rightRotate(t.right)
                return self.__leftRotate(t)
            elif t.right.right.height >= t.right.left.height:
                return self.__leftRotate(t)
            else:
                t.right = self.__rightRotate(t.right)
                return self.__leftRotate(t)
        # when left side is heavier
        elif balance < -1:
            if t.left.right is None:
                return self.__rightRotate(t)
            elif t.left.left is None:
                t.left = self.__leftRotate(t.left)
                return self.__rightRotate(t)
            elif t.left.left.height >= t.left.right.height:
                return self.__rightRotate(t)
            else:
                t.left = self.__leftRotate(t.left)
                return self.__rightRotate(t)

    def __leftRotate(self, curNode):
        x = curNode.right
        y = x.left
        # left rotation
        x.left = curNode
        # move floater
        curNode.right = y
        # update old root's height
        if curNode.left is None and curNode.right is None:
            curNode.height = 1
        elif curNode.left is None:
            curNode.height = curNode.right.height + 1
        elif curNode.right is None:
            curNode.height = curNode.left.height + 1
        else:
            curNode.height = max(curNode.left.height, curNode.right.height) + 1
        # update new root's height
        if x.left is None:
            x.height = x.right.height + 1
        elif x.right is None:
            x.height = x.left.height + 1
        elif x.left.height > x.right.height:
            x.height = x.left.height + 1
        else:
            x.height = x.right.height + 1
        return x

    def __rightRotate(self, curNode):
        x = curNode.left
        y = x.right
        # right rotation
        x.right = curNode
        # move floater
        curNode.left = y
        # update old root's height
        if curNode.left is None and curNode.right is None:
            curNode.height = 1
        elif curNode.left is None:
            curNode.height = curNode.right.height + 1
        elif curNode.right is None:
            curNode.height = curNode.left.height + 1
        else:
            curNode.height = max(curNode.left.height, curNode.right.height) + 1
        # update new root's height
        if x.left is None:
            x.height = x.right.height + 1
        elif x.right is None:
            x.height = x.left.height + 1
        elif x.left.height > x.right.height:
            x.height = x.left.height + 1
        else:
            x.height = x.right.height + 1
        return x

    def in_order(self):
        # Construct and return a string representing the in-order
        # traversal of the tree. Empty trees should be printed as [ ].
        # Trees with one value should be printed as [ 4 ]. Trees with more
        # than one value should be printed as [ 4, 7 ]. Note the spacing.
        # Your solution must be recursive. This will involve the introduction
        # of additional private methods to support the recursion control
        # variable.
        if self.__rin_order(self.__root) == "":
            return "[ ]"
        else:
            return "[ " + self.__rin_order(self.__root)[0:-2] + " ]"

    def __rin_order(self, root):
        String = ""
        if root is None:
            return String
        else:
            String += self.__rin_order(root.left)
            String = String + str(root.value) + ', '
            String += self.__rin_order(root.right)
        return String

    def pre_order(self):
        # Construct and return a string representing the pre-order
        # traversal of the tree. Empty trees should be printed as [ ].
        # Trees with one value should be printed in as [ 4 ]. Trees with
        # more than one value should be printed as [ 4, 7 ]. Note the spacing.
        # Your solution must be recursive. This will involve the introduction
        # of additional private methods to support the recursion control
        # variable.
        if self.__rpre_order(self.__root) == "":
            return "[ ]"
        else:
            return "[ " + self.__rpre_order(self.__root)[0:-2] + " ]"

    def __rpre_order(self, root):
        String = ""
        if root:
            String = String + str(root.value) + ', '
            String += self.__rpre_order(root.left)
            String += self.__rpre_order(root.right)
        return String

    def post_order(self):
        # Construct an return a string representing the post-order
        # traversal of the tree. Empty trees should be printed as [ ].
        # Trees with one value should be printed in as [ 4 ]. Trees with
        # more than one value should be printed as [ 4, 7 ]. Note the spacing.
        # Your solution must be recursive. This will involve the introduction
        # of additional private methods to support the recursion control
        # variable.
        if self.__rpost_order(self.__root) == "":
            return "[ ]"
        else:
            return "[ " + self.__rpost_order(self.__root)[0:-2] + " ]"

    def __rpost_order(self, root):
        String = ""
        if root:
            String += self.__rpost_order(root.left)
            String += self.__rpost_order(root.right)
            String = String + str(root.value) + ', '
        return String

    def to_list(self):
        treelist = []
        finallist = self.__rto_list(self.__root, treelist)
        return finallist

    def __rto_list(self, root, list):
        if root is None:
            return list
        else:
            self.__rto_list(root.left, list)
            list.append(root.value)
            self.__rto_list(root.right, list)
        return list

    def get_height(self):
        # return an integer that represents the height of the tree.
        # assume that an empty tree has height 0 and a tree with one
        # node has height 1. This method must operate in constant time.
        if self.__root is None:
            return 0
        else:
            return self.__root.height

    def __str__(self):
        return self.in_order()


if __name__ == '__main__':
    pass
