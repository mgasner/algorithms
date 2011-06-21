def insertion_sort_rev(arr):
  for i in range(len(arr)):
    j = i
    while (j > 0) and (arr[j] > arr[j - 1]):
      x = arr[j]
      arr[j] = arr[j - 1]
      arr[j - 1] = x
      j = j - 1
  return arr