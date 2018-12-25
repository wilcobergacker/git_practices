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


def fibonacci(n):
  fibs = [0,1]
  if n <= len(fibs) - 1:
    return fibs[n]
  else:
    while n > len(fibs) - 1:
      next_fib = fibs[-1] + fibs[-2]
      fibs.append(next_fib)
    return fibs[n]


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)
