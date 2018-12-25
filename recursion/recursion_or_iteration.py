def factorial(n):
  result = 1
  while n != 0:
    result = result * n
    n -= 1
  return result

# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)
