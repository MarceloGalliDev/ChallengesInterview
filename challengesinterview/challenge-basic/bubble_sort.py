def bubble_sort(list_number):
  n = len(list_number)
  for i in range(n):
    for j in range(0, n-i-1):
      if list_number[j] > list_number[j+1]:
        list_number[j], list_number[j+1] = list_number[j+1], list_number[j]
  return list_number

# Test cases
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
print(bubble_sort([5, 1, 4, 2, 8]))