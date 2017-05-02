class Node:


    def __init__(self, data):
        self.__left = None
        self.__right = None
        self.__data = data
        

    def insert(self, data):
        if self.__data:
            if data < self.__data:
                if self.__left is None:
                    self.__left = Node(data)
                else:
                    self.__left.insert(data)
            elif data > self.__data:
                if self.__right is None:
                    self.__right = Node(data)
                else:
                    self.__right.insert(data)
        else:
            self.__data = data
            

    def children_count(self):
        cnt = 0
        if self.__left:
            cnt += 1
        if self.__right:
            cnt += 1
        return cnt
    
    def print_tree(self):
        if self.__left:
            self.__left.print_tree()
        print(self.__data)
        if self.__right:
            self.__right.print_tree()

    def min(self):
        if self.__left is None:
            return self.__data
        else:
            return self._left.min()

    def max(self):
        if self.__right is None:
            return self.__data
        else:
            return self._right.max()

root = Node(8)

root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

root.print_tree()
print("number of children ", root.children_count())

