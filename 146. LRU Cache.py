"""

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.


"""


class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.content = {}
        self.headNode = Node(None, None)
        self.lastNode = Node(None, None)
        self.headNode.next, self.lastNode.prev = self.lastNode, self.headNode


    '''
        head -> 1 -> 2 -> last
        
        update 2 as most recent:
        head.next = 2
        2.next = 1
        
        last.prev = 1
        1.next = last
    '''
    def updateAsMostRecentlyUsed(self, node):

        originalPrevNode, originalNextNode = node.prev, node.next
        if originalPrevNode and originalNextNode:
            originalPrevNode.next, originalNextNode.prev = originalNextNode, originalPrevNode

        originalNextOfHead = self.headNode.next
        node.next, originalNextOfHead.prev = originalNextOfHead, node

        node.prev,  self.headNode.next = self.headNode, node

    def removeLast(self):
        toBeRemoved = self.lastNode.prev
        self.content.pop(toBeRemoved.key)

        prev = toBeRemoved.prev
        prev.next = self.lastNode
        self.lastNode.prev = prev

    def get(self, key: int) -> int:
        if key not in self.content:
            return -1

        ''' TODO: update as most recently used content '''
        node = self.content[key]
        self.updateAsMostRecentlyUsed(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.content:
            node = self.content[key]
        else:
            ''' TOOO: check size of content and remove the least recent used if full '''
            if len(self.content) == self.capacity:
                self.removeLast()

        ''' TODO: update as most recently used content '''
        self.updateAsMostRecentlyUsed(node)

        self.content[key] = node

    @staticmethod
    def test():
        cmds =  [
                    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
                    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
                ]
        vals =  [
                    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
                    [[3], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
                ]

        if len(cmds) != len(vals):
            print("INVALID TEST CASE, cmd != val")
            return

        for i in range(len(cmds)):
            print("RUNNING TEST!", i)
            cmd = cmds[i]
            val = vals[i]
            if len(cmd) != len(val):
                print("INVALID TEST CASE!!", i)
                continue

            obj = None
            for j in range(len(cmd)):
                c = cmd[j]
                v = val[j]
                if c == "LRUCache":
                    obj = LRUCache(v[0])
                elif c == "put":
                    print("PUTTING", v[0], v[1])
                    obj.put(v[0], v[1])
                elif c == "get":
                    print("GETTING", v[0])
                    print("--- GET", obj.get(v[0]))

                for k, v in obj.content.items():
                    print("--- after { ", k, ": ", v.val, " }")
                print("--- most recent", obj.headNode.next.val)
                print("--- last", obj.lastNode.prev.val)
                print("")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

LRUCache.test()
