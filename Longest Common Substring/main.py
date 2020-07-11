def find_LBS_length(nums):
  maxLength = 0
  for i in range(len(nums)):
    c1 = find_LDS_length(nums, i, -1)
    c2 = find_LDS_length_rev(nums, i, -1)
    maxLength = max(maxLength, c1 + c2 - 1)
  return maxLength

# find the longest decreasing subsequence from currentIndex till the end of the array


def find_LDS_length(nums,  currentIndex, previousIndex):
  if currentIndex == len(nums):
    return 0

  # include nums[currentIndex] if it is smaller than the previous number
  c1 = 0
  if previousIndex == -1 or nums[currentIndex] < nums[previousIndex]:
    c1 = 1 + find_LDS_length(nums, currentIndex + 1, currentIndex)

  # excluding the number at currentIndex
  c2 = find_LDS_length(nums, currentIndex + 1, previousIndex)

  return max(c1, c2)

# find the longest decreasing subsequence from currentIndex till the beginning of the array


def find_LDS_length_rev(nums,  currentIndex,  previousIndex):
  if currentIndex < 0:
    return 0

  # include nums[currentIndex] if it is smaller than the previous number
  c1 = 0
  if previousIndex == -1 or nums[currentIndex] < nums[previousIndex]:
    c1 = 1 + find_LDS_length_rev(nums, currentIndex - 1, currentIndex)

  # excluding the number at currentIndex
  c2 = find_LDS_length_rev(nums, currentIndex - 1, previousIndex)

  return max(c1, c2)


def main():
  print(find_LBS_length([4, 2, 3, 6, 10, 1, 12]))
  print(find_LBS_length([4, 2, 5, 9, 7, 6, 10, 3, 1]))


main()