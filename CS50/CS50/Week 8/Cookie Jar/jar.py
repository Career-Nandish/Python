from emoji import emojize

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return ("🍪" * self.size)

    def deposit(self, n):
        self.size += n
        return self.size

    def withdraw(self, n):
        self.size -= n
        return self.size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError(f"The jar capacity must be a non-negative integer.")
        self._capacity = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if n < 0 or self.capacity < n:
            raise ValueError(f"Can not store/remove {n} cookie(s) from the jar.")
        self._size = n