def groupSum(start, nums, target):
    # Base case: if target is 0, it means we have found a valid group
    if target == 0:
        return True
    # Base case: if start index exceeds array length, no valid group found
    if start >= len(nums):
        return False

    # Recursive cases: two possibilities, either include current element or exclude it
    # If including current element leads to a valid group, return True
    if groupSum(start + 1, nums, target - nums[start]):
        return True
    # If excluding current element leads to a valid group, return True
    if groupSum(start + 1, nums, target):
        return True

    # If neither including nor excluding current element leads to a valid group, return False
    return False


def splitArray(arr):
    return recursive_helper(1, arr, arr[0])


def recursive_helper(i, arr, target):
    # if we have exhausted the arr
    if i >= len(arr):
        return False
    # we use groupSum recursion to meet the target
    elif groupSum(i, arr, target):
        return True
    # we increment the start and target subarray
    return recursive_helper(i + 1, arr, target + arr[i])


# Test cases
print(splitArray([2, 2]))  # Output: True
print(splitArray([2, 3]))  # Output: False
print(splitArray([5, 2, 3]))  # Output: True
print(splitArray([5, 2, 7]))  # Output: True

