def find_LAS_length(nums):
  # we have to start with two recursive calls, one where we will consider that the first element is
  # bigger than the second element and one where the first element is smaller than the second element
  return max(find_LAS_length_recursive(nums, -1, 0, True), find_LAS_length_recursive(nums, -1, 0, False))


def find_LAS_length_recursive(nums,  previousIndex,  currentIndex,  isAsc):
  if currentIndex == len(nums):
    return 0

  c1 = 0
  # if ascending, the next element should be bigger
  if isAsc:
    if previousIndex == -1 or nums[previousIndex] < nums[currentIndex]:
      c1 = 1 + find_LAS_length_recursive(nums, currentIndex, currentIndex + 1, not isAsc)
  else:  # if descending, the next element should be smaller
    if previousIndex == -1 or nums[previousIndex] > nums[currentIndex]:
      c1 = 1 + find_LAS_length_recursive(nums, currentIndex, currentIndex + 1, not isAsc)
  # skip the current element
  c2 = find_LAS_length_recursive(
    nums, previousIndex, currentIndex + 1, isAsc)
  return max(c1, c2)


def main():
  print(find_LAS_length([1, 2, 3, 4]))
  print(find_LAS_length([3, 2, 1, 4]))
  print(find_LAS_length([1, 3, 2, 4]))


main()