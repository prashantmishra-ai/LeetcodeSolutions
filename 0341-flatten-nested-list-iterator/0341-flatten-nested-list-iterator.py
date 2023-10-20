# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        # Helper function to flatten the nested list
        def flatten(nested):
            flat_list = []
            for item in nested:
                if item.isInteger():
                    flat_list.append(item.getInteger())
                else:
                    flat_list.extend(flatten(item.getList()))
            return flat_list
        
        self.flattened_list = flatten(nestedList)
        self.index = 0  # Pointer to current position in flattened list

    def next(self) -> int:
        # Return the current element and move the pointer to the next
        val = self.flattened_list[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        # Check if the pointer is within bounds of the flattened list
        return self.index < len(self.flattened_list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())