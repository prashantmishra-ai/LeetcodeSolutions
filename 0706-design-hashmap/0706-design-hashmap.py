class ListNode:

    def __init__(self, key, val):

        self.pair = (key, val)

        self.next = None



class MyHashMap:



    def __init__(self):

        """

        Initialize your data structure here.

        """

        self.m = 1000  # size of the array

        self.h = [None] * self.m  # initialize array with None



    def put(self, key: int, value: int) -> None:

        """

        value will always be non-negative.

        """

        index = key % self.m

        if self.h[index] is None:

            # no collision, create a new linked list

            self.h[index] = ListNode(key, value)

        else:

            # collision, traverse the linked list to update value or append a new node

            curr = self.h[index]

            while True:

                if curr.pair[0] == key:

                    # update the value of existing key

                    curr.pair = (key, value)

                    return

                if curr.next is None:

                    # reach the end of the linked list, append a new node

                    break

                curr = curr.next

            curr.next = ListNode(key, value)



    def get(self, key: int) -> int:

        """

        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key

        """

        index = key % self.m

        curr = self.h[index]

        while curr:

            if curr.pair[0] == key:

                return curr.pair[1]

            curr = curr.next

        return -1  # key not found



    def remove(self, key: int) -> None:

        """

        Removes the mapping of the specified value key if this map contains a mapping for the key

        """

        index = key % self.m

        curr = prev = self.h[index]

        if not curr:

            return  # key not found

        if curr.pair[0] == key:

            # the key is in the first node

            self.h[index] = curr.next

        else:

            # search for the key in the linked list

            curr = curr.next

            while curr:

                if curr.pair[0] == key:

                    prev.next = curr.next  # remove the node

                    return

                curr, prev = curr.next, prev.next


