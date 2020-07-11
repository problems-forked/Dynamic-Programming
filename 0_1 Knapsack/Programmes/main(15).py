def find_target_subsets(num, s):
  totalSum = sum(num)

  # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s +totalSum) / 2'
  if totalSum < s or (s + totalSum) % 2 == 1:
    return 0

  return count_subsets(num, int((s + totalSum) / 2))


# this function is exactly similar to what we have in 'Count of Subset Sum' problem
def count_subsets(num, sum):
  n = len(num)
  dp = [0 for x in range(sum+1)]
  dp[0] = 1

  # with only one number, we can form a subset only when the required sum is equal to the number
  for s in range(1, sum+1):
    dp[s] = 1 if num[0] == s else 0

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(sum, -1, -1):
      if s >= num[i]:
        dp[s] += dp[s - num[i]]

  return dp[sum]


def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
