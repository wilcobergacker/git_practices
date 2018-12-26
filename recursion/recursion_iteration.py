# Linear - O(N)
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n

sum_digits(12)
# 1 + 2
# 3
sum_digits(552)
# 5 + 5 + 2
# 12
sum_digits(123456789)

#_____________________________________________________#
def sum_digits(n):
  if n <= 9:
    return n
  last_digit = n % 10
  return sum_digits(n // 10) + last_digit

# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)

#_____________________________________________________
def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min

find_min([42, 17, 2, -1, 67])
# -1
find_mind([])
# None
find_min([13, 72, 19, 5, 86])
#_____________________________________________________

def find_min(a_list, min = None):
  if len(a_list) == 0:
    return min
  else:
    if min == None or a_list[0] < min:
      min = a_list[0]
  return find_min(a_list[1:], min)


# test cases
print(find_min([-1, 2, 3]))
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)

#_____________________________________________________
def is_palindrome(my_string):
  string_length = len(my_string)
  middle_index = string_length // 2
    for index in range(0, middle_index):
      opposite_character_index = string_length - index
      if my_string[index] != my_string[opposite_character_index]
    return False
return True

#_____________________________________________________
def is_palindrome(my_string):
  if len(my_string) < 2:
    return True
  else:
    if my_string[0] != my_string[-1]:
      return False
  return is_palindrome(my_string[1:-1])


# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)

#_____________________________________________________
def multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result

multiplication(3, 7)
# 21
multiplication(5, 5)
# 25
multiplication(0, 4)
# 0

#_____________________________________________________

def multiplication(num_1, num_2):
  result = 0
  if num_1 == 0 or num_2 == 0:
    return 0
  return num_1 + multiplication(num_1, num_2 - 1)


# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)
