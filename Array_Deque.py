from Deque import Deque


class Array_Deque(Deque):

    def __init__(self):
        # capacity starts at 1; we will grow on demand.
        self.__capacity = 1
        self.__contents = [None] * self.__capacity
        # TODO replace pass with any additional initializations you need.
        self.__front = 0
        self.__back = 0

    def __str__(self):
        # TODO replace pass with an implementation that returns a string of
        # exactly the same format as the __str__ method in the Linked_List_Deque.
        # Orient your string from front (left) to back (right).
        if len(self) == 0:
            return '[ ]'
        else:
            string = '[ ' + str(self.__contents[self.__front])
            for i in range(1, len(self)):
                string += ', ' + str(self.__contents[(self.__front + i) % self.__capacity])
            string += ' ]'
            return string

    def __len__(self):
        # TODO replace pass with an implementation that returns the number of
        # items in the deque. This method must run in constant time.
        if self.__front - self.__back == 0:
            if self.__contents[self.__front] is None:
                return 0
            else:
                return 1
        else:
            if self.__front < self.__back:
                return self.__back - self.__front + 1
            else:
                return self.__capacity - (self.__front - self.__back) + 1

    def __grow(self):
        # TODO replace pass with an implementation that doubles the capacity
        # and positions existing items in the deque starting in cell 0 (why is
        # necessary?)
        self.__capacity = self.__capacity * 2
        copy = [None] * self.__capacity
        counter = 0
        tracker = self.__front
        back = len(self.__contents)-1
        while counter != len(self.__contents):
            copy[counter] = self.__contents[tracker % (len(self.__contents))]
            counter += 1
            tracker += 1
        self.__contents = copy
        self.__front = 0
        self.__back = back

    def push_front(self, val):
        # TODO replace pass with your implementation, growing the array before
        # pushing if necessary.
        if len(self) + 1 > self.__capacity:
            self.__grow()
        if len(self) == 0:
            self.__contents[self.__front] = val
        else:
            self.__contents[(self.__front - 1 + self.__capacity) % self.__capacity] = val
            self.__front = (self.__front - 1 + self.__capacity) % self.__capacity

    def pop_front(self):
        # TODO replace pass with your implementation. Do not reduce the capacity.
        if len(self) == 0:
            return None
        elif len(self) == 1:
            val = self.__contents[self.__front]
            self.__contents[self.__front] = None
            return val
        else:
            val = self.__contents[self.__front]
            self.__front = (self.__front + 1 + self.__capacity) % self.__capacity
            return val

    def peek_front(self):
        # TODO replace pass with your implementation.
        if len(self) == 0:
            return None
        else:
            return self.__contents[self.__front]

    def push_back(self, val):
        # TODO replace pass with your implementation, growing the array before
        # pushing if necessary.
        if len(self) + 1 > self.__capacity:
            self.__grow()
        if len(self) == 0:
            self.__contents[self.__back] = val
        else:
            self.__contents[(self.__back + 1 + self.__capacity) % self.__capacity] = val
            self.__back = (self.__back + 1 + self.__capacity) % self.__capacity

    def pop_back(self):
        # TODO replace pass with your implementation. Do not reduce the capacity.
        if len(self) == 0:
            return None
        elif len(self) == 1:
            val = self.__contents[self.__back]
            self.__contents[self.__back] = None
            return val
        else:
            val = self.__contents[self.__back]
            self.__back = (self.__back - 1 + self.__capacity) % self.__capacity
            return val

    def peek_back(self):
        # TODO replace pass with your implementation.
        return self.__contents[self.__back]

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':

