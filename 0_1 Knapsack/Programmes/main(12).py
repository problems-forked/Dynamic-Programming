def count_subsets(num, sum):
  # create a two dimensional array for Memoization, each element is initialized to '-1'
  dp = [[-1 for x in range(sum+1)] for y in range(len(num))]
  return count_subsets_recursive(dp, num, sum, 0)


def count_subsets_recursive(dp, num, sum, currentIndex):
  # base checks
  if sum == 0:
    return 1

  n = len(num)
  if n == 0 or currentIndex >= n:
    return 0

  # check if we have not already processed a similar problem
  if dp[currentIndex][sum] == -1:
    # recursive call after choosing the number at the currentIndex
    # if the number at currentIndex exceeds the sum, we shouldn't process this
    sum1 = 0
    if num[currentIndex] <= sum:
      sum1 = count_subsets_recursive(
        dp, num, sum - num[currentIndex], currentIndex + 1)

    # recursive call after excluding the number at the currentIndex
    sum2 = count_subsets_recursive(dp, num, sum, currentIndex + 1)

    dp[currentIndex][sum] = sum1 + sum2

  return dp[currentIndex][sum]


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()