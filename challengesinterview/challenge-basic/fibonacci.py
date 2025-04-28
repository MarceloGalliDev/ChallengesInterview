def fibonacci_1(n):
  """
  Returns the Fibonacci number.
  The Fibonacci sequence is defined as:
  F(0) = 0
  F(1) = 1
  F(n) = F(n-1) + F(n-2) for n > 1
  """
  if n < 0:
    raise ValueError("Input should be a non-negative integer.")
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    a, b = 0, 1
    for _ in range(n):
      print(a, end=" ")
      a, b = b, a + b

def fibonacci_2(n):
  if n<= 1:
    return n
  else:
    return fibonacci_2(n-1) + fibonacci_2(n-2)

  # Example usage:
  for i in range(10):
    print(fibonacci_2(i), end=" ")