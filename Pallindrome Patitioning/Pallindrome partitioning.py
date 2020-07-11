def find_MPP_cuts(st):
  n = len(st)
  dp = [[-1 for _ in range(n)] for _ in range(n)]
  dpIsPalindrome = [[-1 for _ in range(n)] for _ in range(n)]
  return find_MPP_cuts_recursive(dp, dpIsPalindrome, st, 0, n - 1)


def find_MPP_cuts_recursive(dp, dpIsPalindrome, st, startIndex, endIndex):

  if startIndex >= endIndex or is_palindrome(dpIsPalindrome, st, startIndex, endIndex):
    return 0

  if dp[startIndex][endIndex] == -1:
    # at max, we need to cut the string into its 'length-1' pieces
    minimumCuts = endIndex - startIndex
    for i in range(startIndex, endIndex+1):
      if is_palindrome(dpIsPalindrome, st, startIndex, i):
        # we can cut here as we have a palindrome from 'startIndex' to 'i'
        minimumCuts = min(
          minimumCuts, 1 + find_MPP_cuts_recursive(dp, dpIsPalindrome, st, i + 1, endIndex))

    dp[startIndex][endIndex] = minimumCuts

  return dp[startIndex][endIndex]


def is_palindrome(dpIsPalindrome, st, x, y):
  if dpIsPalindrome[x][y] == -1:
    dpIsPalindrome[x][y] = 1
    i, j = x, y
    while i < j:
      if st[i] != st[j]:
        dpIsPalindrome[x][y] = 0
        break
      i += 1
      j -= 1
      # use memoization to find if the remaining string is a palindrome
      if i < j and dpIsPalindrome[i][j] != -1:
        dpIsPalindrome[x][y] = dpIsPalindrome[i][j]
        break

  return True if dpIsPalindrome[x][y] == 1 else False


def main():
  print(find_MPP_cuts("abdbca"))
  print(find_MPP_cuts("cdpdd"))
  print(find_MPP_cuts("pqr"))
  print(find_MPP_cuts("pp"))
  print(find_MPP_cuts("madam"))


main()