def count_change(denominations, total):
  return count_change_recursive(denominations, total, 0)


def count_change_recursive(denominations, total, currentIndex):
  # base checks
  if total == 0:
    return 1

  n = len(denominations)
  if n == 0 or currentIndex >= n:
    return 0

  # recursive call after selecting the coin at the currentIndex
  # if the coin at currentIndex exceeds the total, we shouldn't process this
  sum1 = 0
  if denominations[currentIndex] <= total:
    sum1 = count_change_recursive(
      denominations, total - denominations[currentIndex], currentIndex)

  # recursive call after excluding the coin at the currentIndex
  sum2 = count_change_recursive(denominations, total, currentIndex + 1)

  return sum1 + sum2


def main():
  print(count_change([1, 2, 3], 5))


main()
