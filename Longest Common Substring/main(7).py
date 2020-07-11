def find_min_operations(s1, s2):
  dp = [[-1 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
  return find_min_operations_recursive(dp, s1, s2, 0, 0)


def find_min_operations_recursive(dp, s1,  s2,  i1,  i2):
  n1, n2 = len(s1), len(s2)
  if dp[i1][i2] == -1:
    # if we have reached the end of s1, then we have to insert all the remaining  characters of s2
    if i1 == n1:
      dp[i1][i2] = n2 - i2

    # if we have reached the end of s2, then we have to delete all the remaining characters of s1
    elif i2 == n2:
      dp[i1][i2] = n1 - i1

    # If the strings have a matching character, we can recursively match for the remaining lengths
    elif s1[i1] == s2[i2]:
      dp[i1][i2] = find_min_operations_recursive(
        dp, s1, s2, i1 + 1, i2 + 1)
    else:
      c1 = find_min_operations_recursive(
        dp, s1, s2, i1 + 1, i2)  # delete
      c2 = find_min_operations_recursive(
        dp, s1, s2, i1, i2 + 1)  # insert
      c3 = find_min_operations_recursive(
        dp, s1, s2, i1 + 1, i2 + 1)  # replace
      dp[i1][i2] = 1 + min(c1, min(c2, c3))

  return dp[i1][i2]


def main():
  print(find_min_operations("bat", "but"))
  print(find_min_operations("abdca", "cbda"))
  print(find_min_operations("passpot", "ppsspqrt"))


main()