def palindrome(text):
  text = text.lower().replace(" ", "")
  return text == text[::-1]

# Test cases
print(palindrome("A base do teto desaba"))