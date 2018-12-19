class HashMap:
  #Create an instance variable called .array, which is a list of size array_size. Make each element of .array equal to None
  def __init__(self, array_size):
    self.array_size = array_size
    
    self.array = [None for item in range(array_size)]
    
  def hash(self, key):
    #.encode() is a string method that converts a string into its corresponding bytes, a list-like object with the numerical representation of each character in the string.
    key_bytes = key.encode()
    #sums the numbers in key_bites
    hash_code = sum(key_bytes)
    return hash_code
	
  def compressor(self, hash_code):
  #Take the modulus of the hash code by the map’s array_size in order to reduce the hash code to a possible index for the array
    return hash_code % self.array_size

    
