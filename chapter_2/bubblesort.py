def bubblesort(A):
  for i in range(len(A)):
    for j in range(len(A)).reverse():
      if (A[j] < A[j - 1]):
        k = A[j - 1]
        A[j - 1] = A[j]
        A[j] = k
  return A