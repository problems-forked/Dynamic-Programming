def find_LAS_length(nums):
  n = len(nums)
  if n == 0:
    return 0
  # dp[i][0] = stores the LAS ending at 'i' such that the last two elements are in ascending order
  # dp[i][1] = stores the LAS ending at 'i' such that the last two elements are in descending order
  dp = [[0 for _ in range(2)] for _ in range(n)]
  maxLength = 1
  for i in range(n):
    # every single element can be considered as LAS of length 1
    dp[i][0] = dp[i][1] = 1
    for j in range(i):
      if nums[i] > nums[j]:
        # if nums[i] is BIGGER than nums[j] then we will consider the LAS ending at 'j' where the
        # last two elements were in DESCENDING order
        dp[i][0] = max(dp[i][0], 1 + dp[j][1])
        maxLength = max(maxLength, dp[i][0])
      elif nums[i] != nums[j]:  # if the numbers are equal don't do anything
        # if nums[i] is SMALLER than nums[j] then we will consider the LAS ending at
        # 'j' where the last two elements were in ASCENDING order
        dp[i][1] = max(dp[i][1], 1 + dp[j][0])
        maxLength = max(maxLength, dp[i][1])
  return maxLength


def main():
  print(find_LAS_length([1, 2, 3, 4]))
  print(find_LAS_length([3, 2, 1, 4]))
  print(find_LAS_length([1, 3, 2, 4]))


main()
