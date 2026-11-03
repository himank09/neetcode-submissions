class ListNode:
    def __init__(self, key: int = -1, val: int = -1, next: 'ListNode' = None):
        self.key = key
        self.val = val
        self.next = next
        
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [ListNode() for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size
        
    def put(self, key: int, value: int) -> None:
        curr = self.buckets[self._hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)
        
    def get(self, key: int) -> int:
        curr = self.buckets[self._hash(key)].next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1
        
    def remove(self, key: int) -> None:
        curr = self.buckets[self._hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)