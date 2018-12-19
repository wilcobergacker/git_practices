class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

#controle of een key in de array leeg is, zo ja plaats hem.
#If current_array_value already has contents, check if the saved key is different from the key we are currently processing. If the keys are the same, overwrite the array value.
#
#If the keys are different, we’re going to implement a way to find the next array index where our key should go. We'll get to handling different keys later.
  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # current_array_value currently holds different key
    return
#de retrieve functie is aangepast, om te checken of de key bestaat en of dezelfde key al aanwezig is.
  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
        return None

    if possible_return_value[0] == key:
        return possible_return_value[1]

    # possible_return_value holds different key
    return
