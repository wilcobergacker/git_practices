#opdracht 1
# define your sum_to_one() function above the function call
def sum_to_one(n):
  result = 1
  call_stack = []
  while n > result:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")

  while len(call_stack) != 0:
    return_value = call_stack.pop()
    print("Return value of {0} adding to result {1}".format(return_value['n_value'], result))
    result += return_value['n_value']
  return result, call_stack

sum_to_one(4)


#opdracht 2
# Define sum_to_one() below...
def sum_to_one(n):
  if n == 1:
    return n
  print("Recursing with input: {0}".format(n))
  return n + sum_to_one(n-1)

# uncomment when you're ready to test
print(sum_to_one(7))


#opdracht 3
# Define factorial() below:
def factorial(n):
  if n <= 1:
    return n
  return n * factorial(n-1)


print(factorial(12))


# define flatten() below...
def flatten(my_list):
  result = []
  for el in my_list:
    if isinstance(el, list):
      print("List found!")
      flat_list = flatten(el)
      result += flat_list
    else:
      result.append(el)
  return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flatten(planets))

# define the fibonacci() function below...
def fibonacci(n):
  if n == 1:
    return 1
  elif n == 0:
    return 0
  else:
    print(fibonacci(n-2))
    print(fibonacci(n-1))
    return fibonacci(n-2) + fibonacci(n-1)




fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"




# Define build_bst() below...
def build_bst(my_list):
  if not my_list:
    return "No Child"
  middle_idx = len(my_list) //2
  middle_value = my_list[middle_idx]
  print("Middle index: " + str(middle_idx))
  print("Middle value: " + str(middle_value))
  tree_node = {"data": middle_value}

  left_value = my_list[middle_idx + 1:]
  right_value = my_list[:middle_idx + 1]

  tree_node["left_child"] = build_bst(my_list[:middle_idx])
  tree_node["right_child"] = build_bst(my_list[middle_idx + 1:])

  return tree_node

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"
