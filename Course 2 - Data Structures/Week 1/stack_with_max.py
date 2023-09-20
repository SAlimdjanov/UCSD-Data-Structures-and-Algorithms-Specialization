""" 
stack_with_max.py

"""


import sys


class StackWithMax:
    """
    Stack with max class

    """

    def __init__(self):
        self.__stack = []
        self.max_value = []

    def push_stack(self, elem):
        """
        Push an element to the stack

        Args:
            elem (int): Query element

        """
        if not self.max_value or elem >= self.max_value[-1]:
            self.max_value.append(elem)
        self.__stack.append(elem)

    def pop_stack(self):
        """
        Pop the stack element

        """
        len_stack = len(self.__stack)
        assert len_stack
        if self.__stack[-1] == self.max_value[-1]:
            self.max_value.pop()
        self.__stack.pop()

    def max_stack(self):
        """
        Obtains maximum stack element

        Returns:
            int: value of the max stack element

        """
        return self.max_value[-1]


if __name__ == "__main__":
    stack = StackWithMax()
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        if query[0] == "push":
            stack.push_stack(int(query[1]))
        elif query[0] == "pop":
            stack.pop_stack()
        elif query[0] == "max":
            print(stack.max_stack())
        else:
            assert 0
