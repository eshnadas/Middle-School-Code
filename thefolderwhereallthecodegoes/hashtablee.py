from LINKLIST import LINKLIST, Node
class HashTable:
  
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
  
    def create_buckets(self):
        return [LINKLIST() for _ in range(self.size)]
    
    # Hash function that creates hashed key
    def hash(self, key):
        a = 1
        index = ord(key[0])
        while a <= len(key)-1:
            index = index * ord(key[a])
            a = a +1
            # print("yayyyyyy !")
        index = index % self.size
        return index
  
    # Insert values into hash map
    def set_val(self, key, val):
        #def hash gives the hash table numbers by multiplying each character (key value) by the next character 
        #(until there are no characters left) and then finds the remainder
        index = self.hash(key)
        bucket = self.hash_table[index]
        #finds all the numbers that go to specific spots 
        a = 0
        while a <= len(self.hash_table):
            node = bucket.findNODEATposiTion(a)
            if node is None:
                break 
            keyValue = node.data
            if keyValue[0] == key:
                #gives first value in keyvalue which is key --> checks if key is paired w a value we want to change
                node.data = [key, val]
                #makes new value (key is not changing bc already looked at the keys value)
                # print("party      ayyyyyyyyyyyyyyyyyy")
                return 
            a = a + 1
        bucket.addTAIl([key, val])
        #print("STOP IT OFJOEWJGOEWJOGECDOIEFIOEWJG")

    # Return searched value with specific key
    def get_val(self, key):
        index = self.hash(key)
        bucket = self.hash_table[index]
        a = 0 
        while a <= len(self.hash_table):
            node = bucket.findNODEATposiTion(a)
            if node is None:
                break 
            keyValue = node.data    
            if keyValue[0] == key:
                return keyValue[1]
            a = a+1
  
    # Remove a value with specific key
    def delete_val(self, key):
        index = self.hash(key)
        bucket = self.hash_table[index]
        a = 0 
        while a <= len(self.hash_table):
            node = bucket.findNODEATposiTion(a)
            if node is None:
                break 
            keyValue = node.data    
            if keyValue[0] == key:
                bucket.delete(a)
            a = a+1
   
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

    def printhashtable(self):
        for bucket in self.hash_table:
            if bucket.numNode != 0: 
                print(bucket)
  
  
hash_table = HashTable(50)

# # insert some values
hash_table.set_val("pogjogai","1")
hash_table.set_val("eaorg","2")
hash_table.set_val("waegiagj","3")
hash_table.set_val("agoiagoijgi","4")
hash_table.set_val("aojwevjawoi","5")
hash_table.set_val("pogjogai","6")
hash_table.set_val("pogjogai","20000000")
hash_table.set_val("iagojgop","123")
hash_table.delete_val("pogjogai")
hash_table.printhashtable()

print()
  
# hash_table.set_val(,)
# print(hash_table)
# print()
  
# # search/access a record with key
# print(hash_table.get_val(,))
# print()
  
# # delete or remove a value
# hash_table.delete_val(,)
# print(hash_table)

