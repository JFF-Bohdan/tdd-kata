class RecentlyUsedList(object):
    def __init__(self, max_list_size=5):
        self._items = []
        self._max_list_size = max_list_size

    def __len__(self):
        return len(self._items)

    def insert(self, item):
        if item is None:
            raise Exception("Null not allowed")

        if (type(item) is str) and (len(item) == 0):
            raise Exception("Empty strings not allowed")

        if item in self._items:
            self._items.remove(item)

        if (self._max_list_size is not None) and (len(self._items) >= self._max_list_size):
            self._items.pop(-1)

        self._items.insert(0, item)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError

        return self._items[index]
