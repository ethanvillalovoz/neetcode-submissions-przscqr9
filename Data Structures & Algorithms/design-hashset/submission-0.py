class MyHashSet:

    def __init__(self):
        self.hashSet = []

    def add(self, key: int) -> None:
        if key not in self.hashSet:
            self.hashSet.append(key)

    def remove(self, key: int) -> None:
        for i, num in enumerate(self.hashSet):
            if num == key:
                self.hashSet.pop(i)

    def contains(self, key: int) -> bool:
        for num in self.hashSet:
            if num == key:
                return True

        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)