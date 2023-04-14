class CreateHashMap:
    def __init__(self, initial_capacity=20):
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    #Inserts/Updates hashtable
    def insert(self, key, item):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        #If key is already in bucket,it will retrieve item via linked list
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        # if not, insert the item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Lookup items in hash table
    def lookup(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None  # no pair[0] matches key 0

    # Hash remove method - removes item from hash table
    def hash_remove(self, key):
        slot = hash(key) % len(self.list)
        destination = self.list[slot]

        # If the key is found in the hash table then remove the item
        if key in destination:
            destination.remove(key)