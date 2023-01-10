class Linked_List:
    class __Node:

        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__size = 0

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        new = Linked_List.__Node(val)
        new.prev = self.__trailer.prev
        self.__trailer.prev.next = new
        new.next = self.__trailer
        self.__trailer.prev = new
        self.__size = self.__size + 1

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        new = Linked_List.__Node(val)
        if index < 0 or index >= self.__len__():
            print("index is out of bound")
            raise IndexError
        counter = 0
        cur = self.__header
        while counter < index:
            cur = cur.next
            counter = counter + 1
        new.prev = cur
        new.next = cur.next
        cur.next.prev = new
        cur.next = new
        self.__size = self.__size + 1

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if index < 0 or index >= self.__len__():
            print("index is out of bound")
            raise IndexError
        value = self.get_element_at(index)
        cur = self.__header
        for i in range(0, index):
            cur = cur.next
        cur.next.next.prev = cur
        cur.next = cur.next.next
        self.__size = self.__size - 1
        return value

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if index < 0 or index >= self.__len__():
            print("index is out of bound")
            raise IndexError
        cur = self.__header.next
        for i in range(0, index):
            cur = cur.next
        return cur.val

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self.__len__() > 1:
            self.append_element(self.remove_element_at(0))

    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        string = ""
        current = self.__header
        while current.next is not self.__trailer:
            if current is self.__header:
                string = string + " " + str(current.next.val)
            else:
                string = string + ", " + str(current.next.val)
            current = current.next
        string = "[" + string + " ]"
        return string

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.__pointer = self.__header
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.__pointer.next is not self.__trailer:
            value = self.__pointer.next.val
            self.__pointer = self.__pointer.next
            return value
        else:
            raise StopIteration

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        reverse = Linked_List()
        cur = self.__trailer.prev
        while cur is not self.__header:
            reverse.append_element(cur.val)
            cur = cur.prev
        reverse.__size = self.__size
        return reverse


if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests
    ll = Linked_List()
    # when the linked list is empty
    print("ll is empty")
    print("print string version of an empty list: " + str(ll))
    print("print string version of an empty list in reverse: " + str(reversed(ll)))
    ll.rotate_left()
    print("print string version of an empty list rotated left by once: " + str(ll))
    print("print size of an empty list: " + str(len(ll)))
        # when the index is out of bound
    try:
        ll.get_element_at(0)
    except IndexError:
        print("getting element at 0: pass")
        print("result: " + str(ll))
    try:
        ll.remove_element_at(0)
    except IndexError:
        print("removing element at 0: pass")
        print("result: " + str(ll))
    try:
        ll.insert_element_at(7,0)
    except IndexError:
        print("inserting element at 0: pass")
        print("result: " + str(ll))
    print("")
    # when the linked list has an element
    ll.append_element(7)
    print("now we have an element!")
    print("print string version of a list with an element: " + str(ll))
    print("print string version of a list with an element in reverse: " + str(reversed(ll)))
    ll.rotate_left()
    print("print string version of a list with an element rotated left by once: " + str(ll))
    print("print size of a list with an element: " + str(len(ll)))
        # when the index is out of bound
    try:
        ll.get_element_at(1)
    except IndexError:
        print("getting element at 1: pass")
        print("result: " + str(ll))
    try:
        ll.remove_element_at(1)
    except IndexError:
        print("removing element at 1: pass")
        print("result: " + str(ll))
    try:
        ll.insert_element_at(7, 1)
    except IndexError:
        print("inserting element at 1: pass")
        print("result: " + str(ll))

        # when the index is in the bound
    print("getting element at 0: " + str(ll.get_element_at(0)))
    print("result: " + str(ll))
    print("removing element at 0: " + str(ll.remove_element_at(0)))
    print("result: " + str(ll))

    print("")

    # when the linked list has more than one element
    ll.append_element(3)
    ll.append_element(2.55)
    ll.append_element(None)
    ll.append_element("Hi there")
    print("now we have several elements in the list!")
    print("print string version of a list with several element: " + str(ll))
    print("print string version of a list with several element in reverse: " + str(reversed(ll)))
    ll.rotate_left()
    print("print string version of a list with several element rotated left by once: " + str(ll))
    print("print size of a list with several element: " + str(len(ll)))
        # when the index is out of bound
    try:
        ll.get_element_at(8)
    except IndexError:
        print("getting element at 8: pass")
        print("result: " + str(ll))
    try:
        ll.remove_element_at(8)
    except IndexError:
        print("removing element at 8: pass")
        print("result: " + str(ll))
    try:
        ll.insert_element_at(7,8)
    except IndexError:
        print("inserting element at 8: pass")
        print("result: " + str(ll))

        # when the index is in the bound
    print("getting element at 3: " + str(ll.get_element_at(3)))
    print("result: " + str(ll))
    print("inserting integer 7 at 3:")
    ll.insert_element_at(7, 3)
    print("result: " + str(ll))
    print("removing element at 3: " + str(ll.get_element_at(3)))
    print("result: " + str(ll))

    print("")

    # iteration Check
    print("Iteration check!")
    print("printing every value in the list: ")
    for val in ll:
        print(val)
    print("")
    print("printing every value in the list in reverse: ")
    for val in reversed(ll):
        print(val)
