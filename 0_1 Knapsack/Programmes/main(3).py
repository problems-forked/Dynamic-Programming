from __future__ import print_function


def solve_knapsack(profits, weights, capacity):
  # basic checks
  n = len(profits)
  if capacity <= 0 or n == 0 or len(weights) != n:
    return 0

  dp = [[0 for x in range(capacity+1)] for y in range(n)]

  # populate the capacity = 0 columns, with '0' capacity we have '0' profit
  for i in range(0, n):
    dp[i][0] = 0

  # if we have only one weight, we will take it if it is not more than the capacity
  for c in range(0, capacity+1):
    if weights[0] <= c:
      dp[0][c] = profits[0]

  # process all sub-arrays for all the capacities
  for i in range(1, n):
    for c in range(1, capacity+1):
      profit1, profit2 = 0, 0
      # include the item, if it is not more than the capacity
      if weights[i] <= c:
        profit1 = profits[i] + dp[i - 1][c - weights[i]]
      # exclude the item
      profit2 = dp[i - 1][c]
      # take maximum
      dp[i][c] = max(profit1, profit2)

  print_selected_elements(dp, weights, profits, capacity)
  # maximum profit will be at the bottom-right corner.
  return dp[n - 1][capacity]


def print_selected_elements(dp, weights, profits, capacity):
  print("Selected weights are: ", end='')
  n = len(weights)
  totalProfit = dp[n-1][capacity]
  for i in range(n-1, 0, -1):
    if totalProfit != dp[i - 1][capacity]:
      print(str(weights[i]) + " ", end='')
      capacity -= weights[i]
      totalProfit -= profits[i]

  if totalProfit != 0:
    print(str(weights[0]) + " ", end='')
  print()


def main():
  print("Total knapsack profit: " +
        str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
  print("Total knapsack profit: " +
        str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


main()