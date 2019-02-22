class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def put(self, key, data):
        hash_value = self.hash_function(key, self.size)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        elif self.slots[hash_value] == key:
            self.data[hash_value] = data
        else:
            next_slot = self.rehash(hash_value, self.size)
            while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot, self.size)

            if self.slots[next_slot] == key:
                self.data[next_slot] = data
            else:
                self.slots[next_slot] = key
                self.data[next_slot] = data

    def get(self, key):
        start_slot = self.hash_function(key, self.size)
        found = True

        next_slot = start_slot

        while self.slots[next_slot] is None or self.slots[next_slot] != key:
            next_slot = self.rehash(next_slot, self.size)
            if next_slot == start_slot:
                found = False
                break
            if self.slots[next_slot] == key:
                break

        if found:
            return self.data[next_slot]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


if __name__ == '__main__':
    hash = HashTable()
    hash[54] = 'cat'
    hash[26] = 'dog'
    hash[93] = 'lion'
    hash[17] = 'tiger'
    hash[77] = 'bird'
    hash[31] = 'cow'
    hash[44] = 'goat'
    hash[55] = 'pig'
    hash[20] = 'chicken'

    print(hash.slots)
    print(hash.data)
    print(hash[17])
    print(hash[20])

    hash[20] = 'duck'
    print(hash[20])
