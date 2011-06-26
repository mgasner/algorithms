def recursive_insertion_sort(L):
  if len(L) == 1:
    return L
  else:
    e = L.pop()
    return insert(e, recursive_insertion_sort(L))
    
def insert(e, L):
  R = []
  while ((len(L) != 0) and (e < L[len(L) - 1])):
    l = L.pop()
    R.insert(0, l)
  L.append(e)
  if (len(R) > 0):
    L = L + R
  return L
