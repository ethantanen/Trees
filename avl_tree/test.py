# to run this test, execute the command "python3 -m unittest -v <this file>"
import avl_tree
import pprint
import unittest
import random


class TestAVLTree(unittest.TestCase):


    # def test_01_insert(self):
    #     avl = avl_tree.AVL()
    #     root = None
    #     for n in [2, 1, 3]:
    #         root = avl.insert(root, n)
    #     all = [i.value for i in avl.get(root)]
    #     assert all == [1, 2, 3] and avl.depth(root) == 2

    def test_02_left_rotate(self):
        avl = avl_tree.AVL()
        root = None
        for n in [1, 2, 3]:
            root = avl.insert(root, n)
        all = [x.value for x in avl.get(root)]
        print(all)
        assert all == [1, 2, 3] and avl.depth(root) == 2

    def test_03_right_rotate(self):
        avl = avl_tree.AVL()
        root = None
        for n in [3, 2, 1]:
            root = avl.insert(root, n)
        all = [i.value for i in avl.get(root)]
        assert all == [1, 2, 3] and avl.depth(root) == 2

    def test_04_left_right_rotate(self):
        avl = avl_tree.AVL()
        root = None
        for n in [2, 1, 5, 3, 4]:
            root = avl.insert(root, n)
        all = [i.value for i in avl.get(root)]
        assert all == [1, 2, 3, 4, 5] and avl.depth(root) == 2

    # def test_05_right_left_rotate(self):
    #     avl = avl_tree.AVL()
    #     root = None
    #     for n in [2, 1, 3]:
    #         root = avl.insert(root, n)
    #     all = [i.value for i in avl.get(root)]
    #     assert all == [1, 2, 3] and avl.depth(root) == 2

    def test_06_random(self):
        avl = avl_tree.AVL()
        root = None
        items = [x for x in random.sample(range(100), 100)]
        for n in items:
            root = avl.insert(root, n)
        all = [i.value for i in avl.get(root)]
        print(all, items.sort())
        assert all == items.sort()
