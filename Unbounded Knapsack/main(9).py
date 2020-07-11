import math


def count_change(denominations, total):
  n = len(denominations)
  dp = [[math.inf for _ in range(total+1)] for _ in range(n)]

  # populate the total=0 columns, as we don't need any coin to make zero total
  for i in range(n):
    dp[i][0] = 0

  for i in range(n):
    for t in range(1, total+1):
      if i > 0:
        dp[i][t] = dp[i - 1][t]  # exclude the coin
      if t >= denominations[i]:
        if dp[i][t - denominations[i]] != math.inf:
          # include the coin
          dp[i][t] = min(dp[i][t], dp[i][t - denominations[i]] + 1)

  # total combinations will be at the bottom-right corner.
  return -1 if dp[n - 1][total] == math.inf else dp[n - 1][total]


def main():
  print(count_change([1, 2, 3], 5))
  print(count_change([1, 2, 3], 11))
  print(count_change([1, 2, 3], 7))
  print(count_change([3, 5], 7))


main()
