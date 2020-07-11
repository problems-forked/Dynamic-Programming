def find_min_operations(s1, s2):
  return find_min_operations_recursive(s1, s2, 0, 0)


def find_min_operations_recursive(s1, s2, i1, i2):

  n1, n2 = len(s1), len(s2)
  # if we have reached the end of s1, then we have to insert all the remaining characters of s2
  if i1 == n1:
    return n2 - i2

  # if we have reached the end of s2, then we have to delete all the remaining characters of s1
  if i2 == n2:
    return n1 - i1

  # If the strings have a matching character, we can recursively match for the remaining lengths
  if s1[i1] == s2[i2]:
    return find_min_operations_recursive(s1, s2, i1 + 1, i2 + 1)

  # perform deletion
  c1 = 1 + find_min_operations_recursive(s1, s2, i1 + 1, i2)
  # perform insertion
  c2 = 1 + find_min_operations_recursive(s1, s2, i1, i2 + 1)
  # perform replacement
  c3 = 1 + find_min_operations_recursive(s1, s2, i1 + 1, i2 + 1)

  return min(c1, min(c2, c3))


def main():
  print(find_min_operations("bat", "but"))
  print(find_min_operations("abdca", "cbda"))
  print(find_min_operations("passpot", "ppsspqrt"))


main()