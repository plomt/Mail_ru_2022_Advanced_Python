"""
lru_cache.py - implementation 
"""


class LruCache:
    """
    LRU-cache class:
    cache results of func for some arguments
    and clear dicts if N-size cache is full
    """

    def __init__(self, n: int):

        self.key_map = {}
        self.queue = []
        self.size = n

    def __getitem__(self, key):
        if key not in self.key_map.keys():
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.key_map[key]

    def __setitem__(self, key, value):
        if key not in self.key_map.keys():
            if len(self.key_map) == self.size:
                key_del = self.queue.pop(0)
                self.key_map.pop(key_del)
            self.key_map[key] = value
            self.queue.append(key)
        else:
            self.key_map[key] = value
            self.queue.remove(key)
            self.queue.append(key)

    def __str__(self):
        return f"[Cache size = {self.size}] dict: {self.key_map}, queue: {self.queue}"

