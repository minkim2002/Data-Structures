import unittest
from Binary_Search_Tree import Binary_Search_Tree
from Fraction import Fraction


class BST_Test(unittest.TestCase):

    def setUp(self):
        self.__bst = Binary_Search_Tree()
        self.__fraction = Fraction(1, 2)

    def test_in_order_empty(self):
        self.assertEqual('[ ]', str(self.__bst.in_order()))

    def test_pre_order_empty(self):
        self.assertEqual('[ ]', str(self.__bst.pre_order()))

    def test_post_order_empty(self):
        self.assertEqual('[ ]', str(self.__bst.post_order()))

    def test_to_list_empty(self):
        self.assertEqual('[]', str(self.__bst.to_list()))

    def test_height_empty(self):
        self.assertEqual(0, self.__bst.get_height())

    def test_in_order_one_node(self):
        self.__bst.insert_element(7)
        self.assertEqual('[ 7 ]', str(self.__bst.in_order()))

    def test_pre_order_one_node(self):
        self.__bst.insert_element(7)
        self.assertEqual('[ 7 ]', str(self.__bst.pre_order()))

    def test_post_order_one_node(self):
        self.__bst.insert_element(7)
        self.assertEqual('[ 7 ]', str(self.__bst.post_order()))

    def test_to_list_one_node(self):
        self.__bst.insert_element(7)
        self.assertEqual('[7]', str(self.__bst.to_list()))

    def test_height_one_node(self):
        self.__bst.insert_element(7)
        self.assertEqual(1, self.__bst.get_height())

    def test_in_order_removal_left_empty_no_balancing(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(7)
        self.__bst.remove_element(4)
        self.assertEqual('[ 7 ]', str(self.__bst.in_order()))

    def test_pre_order_removal_left_empty_no_balancing(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(7)
        self.__bst.remove_element(4)
        self.assertEqual('[ 7 ]', str(self.__bst.pre_order()))

    def test_post_order_removal_left_empty_no_balancing(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(7)
        self.__bst.remove_element(4)
        self.assertEqual('[ 7 ]', str(self.__bst.post_order()))

    def test_to_list_removal_left_empty_no_balancing(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(7)
        self.__bst.remove_element(4)
        self.assertEqual('[7]', str(self.__bst.to_list()))

    def test_in_order_removal_right_empty_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.remove_element(7)
        self.assertEqual('[ 4 ]', str(self.__bst.in_order()))

    def test_pre_order_removal_right_empty_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.remove_element(7)
        self.assertEqual('[ 4 ]', str(self.__bst.pre_order()))

    def test_post_order_removal_right_empty_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.remove_element(7)
        self.assertEqual('[ 4 ]', str(self.__bst.post_order()))

    def test_to_list_removal_right_empty_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.remove_element(7)
        self.assertEqual('[4]', str(self.__bst.to_list()))

    def test_in_order_removal_both_existing_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(8)
        self.__bst.remove_element(7)
        self.assertEqual('[ 4, 8, 10 ]', str(self.__bst.in_order()))

    def test_pre_order_removal_both_existing_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(8)
        self.__bst.remove_element(7)
        self.assertEqual('[ 8, 4, 10 ]', str(self.__bst.pre_order()))

    def test_post_order_removal_both_existing_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(8)
        self.__bst.remove_element(7)
        self.assertEqual('[ 4, 10, 8 ]', str(self.__bst.post_order()))

    def test_to_list_removal_both_existing_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(8)
        self.__bst.remove_element(7)
        self.assertEqual('[4, 8, 10]', str(self.__bst.to_list()))

    def test_in_order_multiple_nodes_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.assertEqual('[ 4, 7, 10 ]', str(self.__bst.in_order()))

    def test_pre_order_multiple_nodes_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.assertEqual('[ 7, 4, 10 ]', str(self.__bst.pre_order()))

    def test_post_order_multiple_nodes_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.assertEqual('[ 4, 10, 7 ]', str(self.__bst.post_order()))

    def test_to_list_multiple_nodes_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.assertEqual('[4, 7, 10]', str(self.__bst.to_list()))

    def test_height_multiple_nodes_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.assertEqual(2, self.__bst.get_height())

    def test_in_order_multiple_nodes2_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.assertEqual('[ 4, 5, 7, 8, 10 ]', str(self.__bst.in_order()))

    def test_pre_order_multiple_nodes2_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.assertEqual('[ 7, 4, 5, 10, 8 ]', str(self.__bst.pre_order()))

    def test_post_order_multiple_nodes2_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.assertEqual('[ 5, 4, 8, 10, 7 ]', str(self.__bst.post_order()))

    def test_to_list_multiple_nodes2_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.assertEqual('[4, 5, 7, 8, 10]', str(self.__bst.to_list()))

    def test_height_multiple_nodes2_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.assertEqual(3, self.__bst.get_height())

    def test_in_order_remove_until_empty(self):
        self.__bst.insert_element(7)
        self.__bst.remove_element(7)
        self.assertEqual('[ ]', str(self.__bst.in_order()))

    def test_pre_order_remove_until_empty(self):
        self.__bst.insert_element(7)
        self.__bst.remove_element(7)
        self.assertEqual('[ ]', str(self.__bst.pre_order()))

    def test_post_order_remove_until_empty(self):
        self.__bst.insert_element(7)
        self.__bst.remove_element(7)
        self.assertEqual('[ ]', str(self.__bst.post_order()))

    def test_to_list_remove_until_empty(self):
        self.__bst.insert_element(7)
        self.__bst.remove_element(7)
        self.assertEqual('[]', str(self.__bst.to_list()))

    def test_height_remove_until_empty(self):
        self.__bst.insert_element(7)
        self.__bst.remove_element(7)
        self.assertEqual(0, self.__bst.get_height())

    def test_in_order_remove_until_one_node(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(5)
        self.__bst.remove_element(5)
        self.assertEqual('[ 7 ]', str(self.__bst.in_order()))

    def test_pre_order_remove_until_one_node(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(5)
        self.__bst.remove_element(5)
        self.assertEqual('[ 7 ]', str(self.__bst.pre_order()))

    def test_post_order_remove_until_one_node(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(5)
        self.__bst.remove_element(5)
        self.assertEqual('[ 7 ]', str(self.__bst.post_order()))

    def test_to_list_remove_until_one_node(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(5)
        self.__bst.remove_element(5)
        self.assertEqual('[7]', str(self.__bst.to_list()))

    def test_height_remove_until_one_node(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(5)
        self.__bst.remove_element(5)
        self.assertEqual(1, self.__bst.get_height())

    def test_in_order_remove_until_multiple_nodes_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(9)
        self.__bst.insert_element(6)
        self.__bst.remove_element(9)
        self.__bst.remove_element(6)
        self.assertEqual('[ 4, 7, 10 ]', str(self.__bst.in_order()))

    def test_pre_order_remove_until_multiple_nodes_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(9)
        self.__bst.insert_element(6)
        self.__bst.remove_element(9)
        self.__bst.remove_element(6)
        self.assertEqual('[ 7, 4, 10 ]', str(self.__bst.pre_order()))

    def test_post_order_remove_until_multiple_nodes_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(9)
        self.__bst.insert_element(6)
        self.__bst.remove_element(9)
        self.__bst.remove_element(6)
        self.assertEqual('[ 4, 10, 7 ]', str(self.__bst.post_order()))

    def test_to_list_remove_until_multiple_nodes_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(9)
        self.__bst.insert_element(6)
        self.__bst.remove_element(9)
        self.__bst.remove_element(6)
        self.assertEqual('[4, 7, 10]', str(self.__bst.to_list()))

    def test_height_remove_until_multiple_nodes_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(9)
        self.__bst.insert_element(6)
        self.__bst.remove_element(9)
        self.__bst.remove_element(6)
        self.assertEqual(2, self.__bst.get_height())

    def test_in_order_remove_until_multiple_nodes2_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.__bst.insert_element(11)
        self.__bst.insert_element(2)
        self.__bst.insert_element(9)
        self.__bst.remove_element(9)
        self.__bst.remove_element(2)
        self.__bst.remove_element(11)
        self.assertEqual('[ 4, 5, 7, 8, 10 ]', str(self.__bst.in_order()))

    def test_pre_order_remove_until_multiple_nodes2_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.__bst.insert_element(11)
        self.__bst.insert_element(2)
        self.__bst.insert_element(9)
        self.__bst.remove_element(9)
        self.__bst.remove_element(2)
        self.__bst.remove_element(11)
        self.assertEqual('[ 7, 4, 5, 10, 8 ]', str(self.__bst.pre_order()))

    def test_post_order_remove_until_multiple_nodes2_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.__bst.insert_element(11)
        self.__bst.insert_element(2)
        self.__bst.insert_element(9)
        self.__bst.remove_element(9)
        self.__bst.remove_element(2)
        self.__bst.remove_element(11)
        self.assertEqual('[ 5, 4, 8, 10, 7 ]', str(self.__bst.post_order()))

    def test_to_list_remove_until_multiple_nodes2_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.__bst.insert_element(11)
        self.__bst.insert_element(2)
        self.__bst.insert_element(9)
        self.__bst.remove_element(9)
        self.__bst.remove_element(2)
        self.__bst.remove_element(11)
        self.assertEqual('[4, 5, 7, 8, 10]', str(self.__bst.to_list()))

    def test_height_remove_until_multiple_nodes2_no_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.__bst.insert_element(11)
        self.__bst.insert_element(2)
        self.__bst.insert_element(9)
        self.__bst.remove_element(9)
        self.__bst.remove_element(2)
        self.__bst.remove_element(11)
        self.assertEqual(3, self.__bst.get_height())

    def test_in_order_multiple_nodes_left_left_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(1)
        self.assertEqual('[ 1, 4, 7 ]', str(self.__bst.in_order()))

    def test_pre_order_multiple_nodes_left_left_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(1)
        self.assertEqual('[ 4, 1, 7 ]', str(self.__bst.pre_order()))

    def test_post_order_multiple_nodes_left_left_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(1)
        self.assertEqual('[ 1, 7, 4 ]', str(self.__bst.post_order()))

    def test_to_list_multiple_nodes_left_left_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(1)
        self.assertEqual('[1, 4, 7]', str(self.__bst.to_list()))

    def test_height_multiple_nodes_left_left_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(1)
        self.assertEqual(2, self.__bst.get_height())

    def test_in_order_multiple_nodes_right_right_balancing(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.__bst.insert_element(7)
        self.assertEqual('[ 1, 4, 7 ]', str(self.__bst.in_order()))

    def test_pre_order_multiple_nodes_right_right_balancing(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.__bst.insert_element(7)
        self.assertEqual('[ 4, 1, 7 ]', str(self.__bst.pre_order()))

    def test_post_order_multiple_nodes_right_right_balancing(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.__bst.insert_element(7)
        self.assertEqual('[ 1, 7, 4 ]', str(self.__bst.post_order()))

    def test_to_list_multiple_nodes_right_right_balancing(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.__bst.insert_element(7)
        self.assertEqual('[1, 4, 7]', str(self.__bst.to_list()))

    def test_height_multiple_nodes_right_right_balancing(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.__bst.insert_element(7)
        self.assertEqual(2, self.__bst.get_height())

    def test_in_order_multiple_nodes_left_right_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.assertEqual('[ 1, 4, 7 ]', str(self.__bst.in_order()))

    def test_pre_order_multiple_nodes_left_right_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.assertEqual('[ 4, 1, 7 ]', str(self.__bst.pre_order()))

    def test_post_order_multiple_nodes_left_right_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.assertEqual('[ 1, 7, 4 ]', str(self.__bst.post_order()))

    def test_to_list_multiple_nodes_left_right_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.assertEqual('[1, 4, 7]', str(self.__bst.to_list()))

    def test_height_multiple_nodes_left_right_balancing(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.assertEqual(2, self.__bst.get_height())

    def test_in_order_multiple_nodes_right_left_balancing(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.assertEqual('[ 1, 4, 7 ]', str(self.__bst.in_order()))

    def test_pre_order_multiple_nodes_right_left_balancing(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.assertEqual('[ 4, 1, 7 ]', str(self.__bst.pre_order()))

    def test_post_order_multiple_nodes_right_left_balancing(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.assertEqual('[ 1, 7, 4 ]', str(self.__bst.post_order()))

    def test_to_list_multiple_nodes_right_left_balancing(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.assertEqual('[1, 4, 7]', str(self.__bst.to_list()))

    def test_height_multiple_nodes_right_left_balancing(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.assertEqual(2, self.__bst.get_height())

    def test_in_order_multiple_nodes_left_left_balancing_after_removal(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(1)
        self.__bst.remove_element(10)
        self.assertEqual('[ 1, 4, 7 ]', str(self.__bst.in_order()))

    def test_pre_order_multiple_nodes_left_left_balancing_after_removal(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(1)
        self.__bst.remove_element(10)
        self.assertEqual('[ 4, 1, 7 ]', str(self.__bst.pre_order()))

    def test_post_order_multiple_nodes_left_left_balancing_after_removal(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(1)
        self.__bst.remove_element(10)
        self.assertEqual('[ 1, 7, 4 ]', str(self.__bst.post_order()))

    def test_to_list_multiple_nodes_left_left_balancing_after_removal(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(1)
        self.__bst.remove_element(10)
        self.assertEqual('[1, 4, 7]', str(self.__bst.to_list()))

    def test_height_multiple_nodes_left_left_balancing_after_removal(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(4)
        self.__bst.insert_element(10)
        self.__bst.insert_element(1)
        self.__bst.remove_element(10)
        self.assertEqual(2, self.__bst.get_height())

    def test_in_order_multiple_nodes_right_right_balancing_after_removal(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.__bst.insert_element(0)
        self.__bst.insert_element(7)
        self.__bst.remove_element(0)
        self.assertEqual('[ 1, 4, 7 ]', str(self.__bst.in_order()))

    def test_pre_order_multiple_nodes_right_right_balancing_after_removal(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.__bst.insert_element(0)
        self.__bst.insert_element(7)
        self.__bst.remove_element(0)
        self.assertEqual('[ 4, 1, 7 ]', str(self.__bst.pre_order()))

    def test_post_order_multiple_nodes_right_right_balancing_after_removal(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.__bst.insert_element(0)
        self.__bst.insert_element(7)
        self.__bst.remove_element(0)
        self.assertEqual('[ 1, 7, 4 ]', str(self.__bst.post_order()))

    def test_to_list_multiple_nodes_right_right_balancing_after_removal(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.__bst.insert_element(0)
        self.__bst.insert_element(7)
        self.__bst.remove_element(0)
        self.assertEqual('[1, 4, 7]', str(self.__bst.to_list()))

    def test_height_multiple_nodes_right_right_balancing_after_removal(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(4)
        self.__bst.insert_element(0)
        self.__bst.insert_element(7)
        self.__bst.remove_element(0)
        self.assertEqual(2, self.__bst.get_height())

    def test_in_order_multiple_nodes_left_right_balancing_after_removal(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(1)
        self.__bst.insert_element(10)
        self.__bst.insert_element(4)
        self.__bst.remove_element(10)
        self.assertEqual('[ 1, 4, 7 ]', str(self.__bst.in_order()))

    def test_pre_order_multiple_nodes_left_right_balancing_after_removal(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(1)
        self.__bst.insert_element(10)
        self.__bst.insert_element(4)
        self.__bst.remove_element(10)
        self.assertEqual('[ 4, 1, 7 ]', str(self.__bst.pre_order()))

    def test_post_order_multiple_nodes_left_right_balancing_after_removal(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(1)
        self.__bst.insert_element(10)
        self.__bst.insert_element(4)
        self.__bst.remove_element(10)
        self.assertEqual('[ 1, 7, 4 ]', str(self.__bst.post_order()))

    def test_to_list_multiple_nodes_left_right_balancing_after_removal(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(1)
        self.__bst.insert_element(10)
        self.__bst.insert_element(4)
        self.__bst.remove_element(10)
        self.assertEqual('[1, 4, 7]', str(self.__bst.to_list()))

    def test_height_multiple_nodes_left_right_balancing_after_removal(self):
        self.__bst.insert_element(7)
        self.__bst.insert_element(1)
        self.__bst.insert_element(10)
        self.__bst.insert_element(4)
        self.__bst.remove_element(10)
        self.assertEqual(2, self.__bst.get_height())

    def test_in_order_multiple_nodes_right_left_balancing_after_removal(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(7)
        self.__bst.insert_element(0)
        self.__bst.insert_element(4)
        self.__bst.remove_element(0)
        self.assertEqual('[ 1, 4, 7 ]', str(self.__bst.in_order()))

    def test_pre_order_multiple_nodes_right_left_balancing_after_removal(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(7)
        self.__bst.insert_element(0)
        self.__bst.insert_element(4)
        self.__bst.remove_element(0)
        self.assertEqual('[ 4, 1, 7 ]', str(self.__bst.pre_order()))

    def test_post_order_multiple_nodes_right_left_balancing_after_removal(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(7)
        self.__bst.insert_element(0)
        self.__bst.insert_element(4)
        self.__bst.remove_element(0)
        self.assertEqual('[ 1, 7, 4 ]', str(self.__bst.post_order()))

    def test_to_list_multiple_nodes_right_left_balancing_after_removal(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(7)
        self.__bst.insert_element(0)
        self.__bst.insert_element(4)
        self.__bst.remove_element(0)
        self.assertEqual('[1, 4, 7]', str(self.__bst.to_list()))

    def test_height_multiple_nodes_right_left_balancing_after_removal(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(7)
        self.__bst.insert_element(0)
        self.__bst.insert_element(4)
        self.__bst.remove_element(0)
        self.assertEqual(2, self.__bst.get_height())

    def test_equal_fraction_true(self):
        self.assertEqual(True, self.__fraction.__eq__(Fraction(1, 2)))

    def test_equal_fraction_true2(self):
        self.assertEqual(True, self.__fraction.__eq__(Fraction(2, 4)))

    def test_equal_fraction_false(self):
        self.assertEqual(False, self.__fraction.__eq__(Fraction(1, 4)))

    def test_equal_fraction_false2(self):
        self.assertEqual(False, self.__fraction.__eq__(Fraction(3, 4)))

    def test_greater_than_fraction_true(self):
        self.assertEqual(True, self.__fraction.__lt__(Fraction(3, 2)))

    def test_greater_than_fraction_true2(self):
        self.assertEqual(True, self.__fraction.__lt__(Fraction(4, 2)))

    def test_greater_than_fraction_false(self):
        self.assertEqual(False, self.__fraction.__lt__(Fraction(1, 4)))

    def test_greater_than_fraction_false2(self):
        self.assertEqual(False, self.__fraction.__lt__(Fraction(1, 2)))

    def test_less_than_fraction_true(self):
        self.assertEqual(True, self.__fraction.__gt__(Fraction(1, 4)))

    def test_less_than_fraction_true2(self):
        self.assertEqual(True, self.__fraction.__gt__(Fraction(2, 8)))

    def test_less_than_fraction_false(self):
        self.assertEqual(False, self.__fraction.__gt__(Fraction(43, 4)))

    def test_less_than_fraction_false2(self):
        self.assertEqual(False, self.__fraction.__gt__(Fraction(1, 2)))

    def test_empty_fraction_tree(self):
        self.assertEqual('[ ]', str(self.__bst.in_order()))

    def test_a_single_fraction_tree(self):
        self.__bst.insert_element(self.__fraction)
        self.assertEqual('[1/2]', str(self.__bst.to_list()))

    def test_multiple_fractions_tree(self):
        self.__bst.insert_element(self.__fraction)
        self.__bst.insert_element(Fraction(2, 3))
        self.__bst.insert_element(Fraction(3, 4))
        self.assertEqual('[1/2, 2/3, 3/4]', str(self.__bst.to_list()))

    def test_multiple_fractions2_tree(self):
        self.__bst.insert_element(self.__fraction)
        self.__bst.insert_element(Fraction(2, 3))
        self.__bst.insert_element(Fraction(3, 4))
        self.__bst.insert_element(Fraction(5, 6))
        self.__bst.insert_element(Fraction(1, 7))
        self.__bst.insert_element(Fraction(13, 25))
        self.assertEqual('[1/7, 1/2, 13/25, 2/3, 3/4, 5/6]', str(self.__bst.to_list()))

    def test_multiple_fractions_with_removal_tree(self):
        self.__bst.insert_element(self.__fraction)
        self.__bst.insert_element(Fraction(2, 3))
        self.__bst.insert_element(Fraction(3, 4))
        self.__bst.insert_element(Fraction(5, 6))
        self.__bst.insert_element(Fraction(1, 7))
        self.__bst.insert_element(Fraction(13, 25))
        self.__bst.remove_element(Fraction(5, 6))
        self.assertEqual('[1/7, 1/2, 13/25, 2/3, 3/4]', str(self.__bst.to_list()))

    def test_multiple_fractions_with_removal2_tree(self):
        self.__bst.insert_element(self.__fraction)
        self.__bst.insert_element(Fraction(2, 3))
        self.__bst.insert_element(Fraction(3, 4))
        self.__bst.insert_element(Fraction(5, 6))
        self.__bst.insert_element(Fraction(1, 7))
        self.__bst.insert_element(Fraction(13, 25))
        self.__bst.remove_element(Fraction(13, 25))
        self.assertEqual('[1/7, 1/2, 2/3, 3/4, 5/6]', str(self.__bst.to_list()))




if __name__ == '__main__':
    unittest.main()
