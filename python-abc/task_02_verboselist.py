#!/usr/bin/python3
"""this Module is about learning abc class """


class VerboseList(list):
    """an VerboseList class"""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        super().extend(x)
        print(f"Extended the list with [{len(x)}] items.")

    def remove(self, item):
        if item not in self:
            raise ValueError(f"{item} not in list")
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, item=-1):
        print(f"Popped [{self[item]}] from the list.")
        item = super().pop(item)
        return item
