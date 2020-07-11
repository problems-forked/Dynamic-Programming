def solve_rod_cutting(lengths, prices, n):
  lengthCount = len(lengths)
  # base checks
  if n <= 0 or lengthCount == 0 or len(prices) != lengthCount:
    return 0

  dp = [[0 for _ in range(n+1)] for _ in range(lengthCount)]

  # process all rod lengths for all prices
  for i in range(lengthCount):
    for length in range(1, n+1):
      p1, p2 = 0, 0
      if lengths[i] <= length:
        p1 = prices[i] + dp[i][length - lengths[i]]
      if i > 0:
        p2 = dp[i - 1][length]
      dp[i][length] = max(p1, p2)

  # maximum price will be at the bottom-right corner.
  return dp[lengthCount - 1][n]


def main():
  print(solve_rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))


main()
