def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

# Test cases
print(gcd(10, 5))
print(f"gcd of 54 and 24: {gcd(54, 24)}")