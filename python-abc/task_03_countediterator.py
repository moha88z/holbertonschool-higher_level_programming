#!/usr/bin/python3
"""this Module is about learning abc class """


class CountedIterator:
    """an CountedIterator class"""

    def __init__(self, iterator, count=0):
        self.iterator = iter(iterator)
        self.count = count

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.count
