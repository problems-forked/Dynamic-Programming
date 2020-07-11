def solve_knapsack(profits, weights, capacity):
  dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]
  return solve_knapsack_recursive(dp, profits, weights, capacity, 0)


def solve_knapsack_recursive(dp, profits, weights, capacity, currentIndex):
  n = len(profits)
  # base checks
  if capacity <= 0 or n == 0 or len(weights) != n or currentIndex >= n:
    return 0

  # check if we have not already processed a similar sub-problem
  if dp[currentIndex][capacity] == -1:
    # recursive call after choosing the items at the currentIndex, note that we
    # recursive call on all items as we did not increment currentIndex
    profit1 = 0
    if weights[currentIndex] <= capacity:
      profit1 = profits[currentIndex] + solve_knapsack_recursive(
        dp, profits, weights, capacity - weights[currentIndex], currentIndex)

    # recursive call after excluding the element at the currentIndex
    profit2 = solve_knapsack_recursive(
      dp, profits, weights, capacity, currentIndex + 1)

    dp[currentIndex][capacity] = max(profit1, profit2)

  return dp[currentIndex][capacity]


def main():
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))


main()