def find_SI(m, n, p):
  return find_SI_recursive({}, m, n, p, 0, 0, 0)


def find_SI_recursive(dp, m, n, p, mIndex, nIndex, pIndex):
  mLen, nLen, pLen = len(m), len(n), len(p)
  # if we have reached the end of the all the strings

  if mIndex == mLen and nIndex == nLen and pIndex == pLen:
    return True

  # if we have reached the end of 'p' but 'm' or 'n' still has some characters left
  if pIndex == pLen:
    return False

  subProblemKey = str(mIndex) + "-" + str(nIndex) + "-" + str(pIndex)
  if subProblemKey not in dp:
    b1, b2 = False, False
    if mIndex < mLen and m[mIndex] == p[pIndex]:
      b1 = find_SI_recursive(dp, m, n, p, mIndex + 1, nIndex, pIndex + 1)

    if nIndex < nLen and n[nIndex] == p[pIndex]:
      b2 = find_SI_recursive(dp, m, n, p, mIndex, nIndex + 1, pIndex + 1)

    dp[subProblemKey] = b1 or b2

  return dp.get(subProblemKey)


def main():
  print(find_SI("abd", "cef", "abcdef"))
  print(find_SI("abd", "cef", "adcbef"))
  print(find_SI("abc", "def", "abdccf"))
  print(find_SI("abcdef", "mnop", "mnaobcdepf"))


main()