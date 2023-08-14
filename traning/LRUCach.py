class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.__list = []
        self.__dict = {}

    def get(self, key: int) -> int:
        if key in self.__dict:
            self.__list.remove(key)
            self.__list.insert(0,key)
            return self.__dict.get(key, -1)

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            if self.capacity == len(self.__list):
                self.__dict.pop(self.__list.pop())
            self.__list.insert(0,key)
