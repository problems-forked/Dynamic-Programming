def find_LAS_length(nums):
  n = len(nums)
  dp = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]
  return max(find_LAS_length_recursive(dp, nums, -1, 0, True),
             find_LAS_length_recursive(dp, nums, -1, 0, False))


def find_LAS_length_recursive(dp, nums, previousIndex, currentIndex,  isAsc):

  if currentIndex == len(nums):
    return 0

  if dp[previousIndex + 1][currentIndex][1 if isAsc else 0] == -1:
    c1 = 0
    # if ascending, the next element should be bigger
    if isAsc:
      if previousIndex == -1 or nums[previousIndex] < nums[currentIndex]:
        c1 = 1 + find_LAS_length_recursive(dp, nums, currentIndex, currentIndex + 1, not isAsc)
    else:  # if descending, the next element should be smaller
      if previousIndex == -1 or nums[previousIndex] > nums[currentIndex]:
        c1 = 1 + find_LAS_length_recursive(dp, nums, currentIndex, currentIndex + 1, not isAsc)

    # skip the current element
    c2 = find_LAS_length_recursive(
      dp, nums, previousIndex, currentIndex + 1, isAsc)
    dp[previousIndex + 1][currentIndex][1 if isAsc else 0] = max(c1, c2)

  return dp[previousIndex + 1][currentIndex][1 if isAsc else 0]


def main():
  print(find_LAS_length([1, 2, 3, 4]))
  print(find_LAS_length([3, 2, 1, 4]))
  print(find_LAS_length([1, 3, 2, 4]))


main()