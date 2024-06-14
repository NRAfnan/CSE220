def merge_lists_recursively(mid_list, final_list, combined_list, m_i, f_i):
    """
       Recursively merges the two lists in descending order.

       Args:
       mid_list: List of midterm exam marks.
       final_list: List of final exam marks.
       combined_list: List to store the merged marks.
       m_i: Index for midterm list.
       f_i: Index for final list.

       Returns:
       List containing merged marks in descending order.
    """
    # Base case: If both lists are exhausted, return the combined list
    if f_i < 0 and m_i < 0:
        return combined_list

    # If there are still elements in the midterm list and either the final list is exhausted
    # or the current midterm mark is greater, append the current midterm mark to the combined list
    # and recursively call the function with the next index in the midterm list.
    if m_i >= 0 and (f_i < 0 or mid_list[m_i] > final_list[f_i]):
        combined_list.append(mid_list[m_i])
        return merge_lists_recursively(mid_list, final_list, combined_list, m_i - 1, f_i)

    # If there are still elements in the final list and either the midterm list is exhausted
    # or the current final mark is greater, append the current final mark to the combined list
    # and recursively call the function with the next index in the final list.
    elif f_i >= 0 and (m_i < 0 or final_list[f_i] > mid_list[m_i]):
        combined_list.append(final_list[f_i])
        return merge_lists_recursively(mid_list, final_list, combined_list, m_i, f_i - 1)


def merge_Lists(mid_list,final_list,combined_list):
    """
    Wrapper function to merge two lists in descending order.

    Args:
    mid_list: List of midterm exam marks.
    final_list: List of final exam marks.
    combined_list: List to store the merged marks.

    Returns:
    List containing merged marks in descending order.
    """
    return merge_lists_recursively(mid_list, final_list, combined_list, len(mid_list) - 1, len(final_list) - 1)


### Driver Code Do not change it ###
mid=[5, 7, 14, 20, 24]
final=[10, 12, 25]
merged_list=merge_Lists(mid,final,[])
print(merged_list)
# This should print [25, 24, 20, 14, 12, 10, 7, 5]

mid=[11, 20, 24, 28]
final=[10, 12]
merged_list=merge_Lists(mid,final,[])
print(merged_list)
# This should print [28, 24, 20, 12, 11, 10]
