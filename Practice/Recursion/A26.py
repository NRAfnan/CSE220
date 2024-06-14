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


# Test cases
print(groupSum(0, [2, 4, 8], 10))  # Output: True
print(groupSum(0, [2, 4, 8], 14))  # Output: True
print(groupSum(0, [2, 4, 8], 9))  # Output: False
