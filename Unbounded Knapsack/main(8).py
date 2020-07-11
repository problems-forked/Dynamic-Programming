import math


def count_change(denominations, total):
  dp = [[-1 for _ in range(total+1)] for _ in range(len(denominations))]
  result = count_change_recursive(dp, denominations, total, 0)
  return -1 if result == math.inf else result


def count_change_recursive(dp, denominations, total, currentIndex):
  # base check
  if total == 0:
    return 0
  n = len(denominations)
  if n == 0 or currentIndex >= n:
    return math.inf

  # check if we have not already processed a similar sub-problem
  if dp[currentIndex][total] == -1:
    # recursive call after selecting the coin at the currentIndex
    # if the coin at currentIndex exceeds the total, we shouldn't process this
    count1 = math.inf
    if denominations[currentIndex] <= total:
      res = count_change_recursive(
        dp, denominations, total - denominations[currentIndex], currentIndex)
      if res != math.inf:
        count1 = res + 1

    # recursive call after excluding the coin at the currentIndex
    count2 = count_change_recursive(
      dp, denominations, total, currentIndex + 1)
    dp[currentIndex][total] = min(count1, count2)

  return dp[currentIndex][total]


def main():
  print(count_change([1, 2, 3], 5))
  print(count_change([1, 2, 3], 11))
  print(count_change([1, 2, 3], 7))
  print(count_change([3, 5], 7))


main()