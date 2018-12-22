from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:

  def __init__(self, size):

    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for node in list_at_array:
      if node[0] == key:
        node[1] = value
        return
    list_at_array.insert(payload)

  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_index = self.array[array_index]
    print(key)
    for node in list_at_index:
      if node[0] == key:
       	print(node[0], node[1])
        return node[1]
    return None

print('Hey')
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  print(flower)
  blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
print(blossom.retrieve('begonia'))
print("hey")
