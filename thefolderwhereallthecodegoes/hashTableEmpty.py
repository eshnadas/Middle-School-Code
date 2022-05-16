class HashTable:
  
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
  
    def create_buckets(self):
        return [[] for _ in range(self.size)]
        # Make buckets linked lists if we have code for them
    
    # Hash function that creates hashed key
    def hash(self, key):
        pass
  
    # Insert values into hash map
    def set_val(self, key, val):
        pass
        
    # Return searched value with specific key
    def get_val(self, key):
        pass
  
    # Remove a value with specific key
    def delete_val(self, key):
        pass
  
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
  
  
hash_table = HashTable(50)

# # insert some values
# hash_table.set_val(,)
# print(hash_table)
# print()
  
# hash_table.set_val(,)
# print(hash_table)
# print()
  
# # search/access a record with key
# print(hash_table.get_val(,))
# print()
  
# # delete or remove a value
# hash_table.delete_val(,)
# print(hash_table)