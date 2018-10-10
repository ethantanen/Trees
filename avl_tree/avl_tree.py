

class Node():
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0
    def __str__(self):
        return "value: " + str(self.value) + " height: " + str(self.height)

class AVL():

    def __init__ (self):
        print('AVL Tree Created!')

    def insert( self, root, value):

        # begin with bst insert while updating heights of nodes on path
        if not root:
            return Node(value)
        elif value < root.value:
            root.height -= 1
            root.left = self.insert(root.left, value)
        else:
            root.height += 1
            root.right = self.insert(root.right, value)

        # balance node if height not in range [-1, 1]
        if root.height < -1 and root.left and value < root.left.value:
            print('right rotate')
            return self.right_rotate(root)

        if root.height < -1 and root.left and value > root.left.value:
            print('left-right rotate')
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if root.height > 1 and root.right and value < root.right.value:
            print('right-left rotate')
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        if root.height > 1 and root.right and value >= root.right.value:
            print('left rotate')
            return self.left_rotate(root)

        return root

    # perform a right rotation rooted on y
    def right_rotate(self, y):

        # perform rotation
        x = y.left
        y.left = x.right
        x.right = y

        # update heights
        x.height = self.get_height(x)
        y.height = self.get_height(y)

        return x

    # perform a left rotation rooted on x
    def left_rotate(self, x):

        # perform rotation
        y = x.right
        x.right = y.left
        y.left = x

        # update heights
        x.height = self.get_height(x)
        y.height = self.get_height(y)

        return y

    # return the max height of the nodes children
    def get_height(self, node):

        left_height = node.left.height if node.left is not None else None
        right_height = node.right.height if node.right is not None else None

        if left_height is None and right_height is None:
            return 0
        if left_height is not None and right_height is None:
            return left_height
        if right_height is not None and left_height is None:
            return right_height
        return max(left_height, right_height)

    # return list of avl trees entries in order
    def get(self, root, result = []):
        if root == None:
            return
        self.get(root.left, result)
        result += [root]
        self.get(root.right, result)
        return result

    # calculate depth of tree
    def depth(self, root, depth=0):

        if root == None:
            return depth

        depth_left = self.depth(root.left, depth+1)
        depth_right = self.depth(root.right, depth+1)

        return max(depth_left, depth_right)
