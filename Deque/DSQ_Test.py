import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue


class DSQTester(unittest.TestCase):

    def setUp(self):
        self.__deque = get_deque()
        self.__stack = Stack()
        self.__queue = Queue()

    def test_empty_deque(self):
        self.assertEqual('[ ]', str(self.__deque))

    def test_push_front_empty_deque(self):
        self.__deque.push_front(1)
        self.assertEqual('[ 1 ]', str(self.__deque))

    def test_push_back_empty_deque(self):
        self.__deque.push_back(1)
        self.assertEqual('[ 1 ]', str(self.__deque))

    def test_push_front_one_element_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.assertEqual('[ 2, 1 ]', str(self.__deque))

    def test_push_back_one_element_deque(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.assertEqual('[ 1, 2 ]', str(self.__deque))

    def test_push_front_multiple_elements_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.assertEqual('[ 5, 4, 3, 2, 1 ]', str(self.__deque))

    def test_push_back_multiple_elements_deque(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.push_back(4)
        self.__deque.push_back(5)
        self.assertEqual('[ 1, 2, 3, 4, 5 ]', str(self.__deque))

    def test_pop_front_empty_deque(self):
        self.__deque.pop_front()
        self.assertEqual('[ ]', str(self.__deque))

    def test_pop_front_empty_return_deque(self):
        self.assertEqual(None, self.__deque.pop_front())

    def test_pop_back_empty_deque(self):
        self.__deque.pop_back()
        self.assertEqual('[ ]', str(self.__deque))

    def test_pop_back_empty_return_deque(self):
        self.assertEqual(None, self.__deque.pop_back())

    def test_pop_front_one_element_deque(self):
        self.__deque.push_front(1)
        self.__deque.pop_front()
        self.assertEqual('[ ]', str(self.__deque))

    def test_pop_front_one_element_return_deque(self):
        self.__deque.push_front(1)
        self.assertEqual(1, self.__deque.pop_front())

    def test_pop_back_one_element_deque(self):
        self.__deque.push_back(1)
        self.__deque.pop_back()
        self.assertEqual('[ ]', str(self.__deque))

    def test_pop_back_one_element_return_deque(self):
        self.__deque.push_back(1)
        self.assertEqual(1, self.__deque.pop_back())

    def test_pop_front_multiple_elements_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.__deque.pop_front()
        self.assertEqual('[ 4, 3, 2, 1 ]', str(self.__deque))

    def test_pop_front_multiple_elements_return_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.assertEqual(5, self.__deque.pop_front())

    def test_pop_back_multiple_elements_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.__deque.pop_back()
        self.assertEqual('[ 5, 4, 3, 2 ]', str(self.__deque))

    def test_pop_back_multiple_elements_return_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.assertEqual(1, self.__deque.pop_back())

    def test_peek_front_empty_deque(self):
        self.__deque.peek_front()
        self.assertEqual('[ ]', str(self.__deque))

    def test_peek_front_empty_return_deque(self):
        self.assertEqual(None, self.__deque.peek_front())

    def test_peek_back_empty_deque(self):
        self.__deque.peek_back()
        self.assertEqual('[ ]', str(self.__deque))

    def test_peek_back_empty_return_deque(self):
        self.assertEqual(None, self.__deque.peek_back())

    def test_peek_front_one_element_deque(self):
        self.__deque.push_front(1)
        self.__deque.peek_front()
        self.assertEqual('[ 1 ]', str(self.__deque))

    def test_peek_front_one_element_return_deque(self):
        self.__deque.push_front(1)
        self.assertEqual(1, self.__deque.peek_front())

    def test_peek_back_one_element_deque(self):
        self.__deque.push_front(1)
        self.__deque.peek_back()
        self.assertEqual('[ 1 ]', str(self.__deque))

    def test_peek_back_one_element_return_deque(self):
        self.__deque.push_front(1)
        self.assertEqual(1, self.__deque.peek_back())

    def test_peek_front_multiple_elements_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.__deque.peek_front()
        self.assertEqual('[ 5, 4, 3, 2, 1 ]', str(self.__deque))

    def test_peek_front_multiple_elements_return_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.assertEqual(5, self.__deque.peek_front())

    def test_peek_back_multiple_elements_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.__deque.peek_back()
        self.assertEqual('[ 5, 4, 3, 2, 1 ]', str(self.__deque))

    def test_peek_back_multiple_elements_return_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.assertEqual(1, self.__deque.peek_back())

    def test_len_empty_deque(self):
        self.assertEqual(0, len(self.__deque))

    def test_len_one_element_deque(self):
        self.__deque.push_front(1)
        self.assertEqual(1, len(self.__deque))

    def test_len_multiple_elements_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_front(4)
        self.__deque.push_front(5)
        self.assertEqual(5, len(self.__deque))

    def test_push_back_pop_back_deque(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.pop_back()
        self.__deque.pop_back()
        self.assertEqual('[ 1 ]', str(self.__deque))

    def test_push_front_pop_front_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.pop_front()
        self.__deque.pop_front()
        self.assertEqual('[ 1 ]', str(self.__deque))

    def test_push_front_pop_back_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.pop_back()
        self.__deque.pop_back()
        self.assertEqual('[ 3 ]', str(self.__deque))

    def test_push_back_pop_front_deque(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.pop_front()
        self.__deque.pop_front()
        self.assertEqual('[ 3 ]', str(self.__deque))

    def test_pop_back_until_empty_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.pop_back()
        self.__deque.pop_back()
        self.__deque.pop_back()
        self.assertEqual('[ ]', str(self.__deque))

    def test_pop_front_until_empty_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.pop_front()
        self.__deque.pop_front()
        self.__deque.pop_front()
        self.assertEqual('[ ]', str(self.__deque))

    def test_peek_ineffective_on_size_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.peek_front()
        self.assertEqual('[ 3, 2, 1 ]', str(self.__deque))

    def test_push_empty_stack(self):
        self.assertEqual('[ ]', str(self.__stack))

    def test_push_one_element_stack(self):
        self.__stack.push(1)
        self.assertEqual('[ 1 ]', str(self.__stack))

    def test_push_multiple_elements_stack(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.push(4)
        self.__stack.push(5)
        self.assertEqual('[ 5, 4, 3, 2, 1 ]', str(self.__stack))

    def test_pop_empty_stack(self):
        self.__stack.pop()
        self.assertEqual('[ ]', str(self.__stack))

    def test_pop_empty_return_stack(self):
        self.assertEqual(None, self.__stack.pop())

    def test_pop_one_element_stack(self):
        self.__stack.push(1)
        self.__stack.pop()
        self.assertEqual('[ ]', str(self.__stack))

    def test_pop_one_element_return_stack(self):
        self.__stack.push(1)
        self.assertEqual(1, self.__stack.pop())

    def test_pop_multiple_elements_stack(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.push(4)
        self.__stack.push(5)
        self.__stack.pop()
        self.assertEqual('[ 4, 3, 2, 1 ]', str(self.__stack))

    def test_pop_multiple_elements_return_stack(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.push(4)
        self.__stack.push(5)
        self.assertEqual(5, self.__stack.pop())

    def test_peek_empty_stack(self):
        self.__stack.peek()
        self.assertEqual('[ ]', str(self.__stack))

    def test_peek_empty_return_stack(self):
        self.assertEqual(None, self.__stack.peek())

    def test_peek_one_element_stack(self):
        self.__stack.push(1)
        self.__stack.peek()
        self.assertEqual('[ 1 ]', str(self.__stack))

    def test_peek_one_element_return_stack(self):
        self.__stack.push(1)
        self.assertEqual(1, self.__stack.peek())

    def test_peek_multiple_elements_stack(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.push(4)
        self.__stack.push(5)
        self.__stack.peek()
        self.assertEqual('[ 5, 4, 3, 2, 1 ]', str(self.__stack))

    def test_peek_multiple_elements_return_stack(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.push(4)
        self.__stack.push(5)
        self.assertEqual(5, self.__stack.peek())

    def test_len_empty_stack(self):
        self.assertEqual(0, len(self.__stack))

    def test_len_one_element_stack(self):
        self.__stack.push(1)
        self.assertEqual(1, len(self.__stack))

    def test_len_multiple_elements_stack(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.push(4)
        self.__stack.push(5)
        self.assertEqual(5, len(self.__stack))

    def test_push_then_pop_stack(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.pop()
        self.__stack.push(3)
        self.__stack.pop()
        self.assertEqual('[ 1 ]', str(self.__stack))

    def test_pop_until_empty_stack(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.pop()
        self.__stack.pop()
        self.__stack.pop()
        self.assertEqual('[ ]', str(self.__stack))

    def test_peek_ineffective_on_size_stack(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.peek()
        self.assertEqual('[ 3, 2, 1 ]', str(self.__stack))

    def test_enqueue_empty_queue(self):
        self.assertEqual('[ ]', str(self.__queue))

    def test_enqueue_one_element_queue(self):
        self.__queue.enqueue(1)
        self.assertEqual('[ 1 ]', str(self.__queue))

    def test_enqueue_multiple_elements_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.__queue.enqueue(5)
        self.assertEqual('[ 1, 2, 3, 4, 5 ]', str(self.__queue))

    def test_dequeue_empty_queue(self):
        self.__queue.dequeue()
        self.assertEqual('[ ]', str(self.__queue))

    def test_dequeue_empty_return_queue(self):
        self.assertEqual(None, self.__queue.dequeue())

    def test_dequeue_one_element_queue(self):
        self.__queue.enqueue(1)
        self.__queue.dequeue()
        self.assertEqual('[ ]', str(self.__queue))

    def test_dequeue_one_element_return_queue(self):
        self.__queue.enqueue(1)
        self.assertEqual(1, self.__queue.dequeue())

    def test_dequeue_multiple_elements_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.__queue.enqueue(5)
        self.__queue.dequeue()
        self.assertEqual('[ 2, 3, 4, 5 ]', str(self.__queue))

    def test_dequeue_multiple_elements_return_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.__queue.enqueue(5)
        self.assertEqual(1, self.__queue.dequeue())

    def test_peek_empty_queue(self):
        self.__queue.peek()
        self.assertEqual('[ ]', str(self.__queue))

    def test_peek_empty_return_queue(self):
        self.assertEqual(None, self.__queue.peek())

    def test_peek_one_element_queue(self):
        self.__queue.enqueue(1)
        self.__queue.peek()
        self.assertEqual('[ 1 ]', str(self.__queue))

    def test_peek_one_element_return_queue(self):
        self.__queue.enqueue(1)
        self.assertEqual(1, self.__queue.peek())

    def test_peek_multiple_elements_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.__queue.enqueue(5)
        self.__queue.peek()
        self.assertEqual('[ 1, 2, 3, 4, 5 ]', str(self.__queue))

    def test_peek_multiple_elements_return_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.__queue.enqueue(5)
        self.assertEqual(1, self.__queue.peek())

    def test_len_empty_queue(self):
        self.assertEqual(0, len(self.__queue))

    def test_len_one_element_queue(self):
        self.__queue.enqueue(1)
        self.assertEqual(1, len(self.__queue))

    def test_len_multiple_elements_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.__queue.enqueue(5)
        self.assertEqual(5, len(self.__queue))

    def test_enqueue_then_dequeue_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.dequeue()
        self.__queue.enqueue(3)
        self.__queue.dequeue()
        self.assertEqual('[ 3 ]', str(self.__queue))

    def test_dequeue_until_empty_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.dequeue()
        self.__queue.dequeue()
        self.__queue.dequeue()
        self.assertEqual('[ ]', str(self.__queue))

    def test_peek_ineffective_on_size_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.peek()
        self.assertEqual('[ 1, 2, 3 ]', str(self.__queue))

    # TODO add your test methods here. Like Linked_List_Test.py,
    # each test should me in a method whose name begins with test_


if __name__ == '__main__':
    unittest.main()
