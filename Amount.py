#Author: Jesus Arias
#GitHub username: ariasje1
#Date: 08/01/2025
#Description: Gives unique combinations that sum to target value
def amount(nums_list, target_sum):
    """
    Finds all unique combinations of numbers from nums_list that sum to target_sum,
    where each number may be used only as many times as it appears in nums_list.

    Parameters:
        nums_list (List[int]): A list of positive integers. Duplicates allowed.
        target_sum (int): The target sum to reach using elements from nums_list.

    Returns:
        List[List[int]]: A list of unique combinations, where each combination is
                         a list of numbers that sum to target_sum.
                         If no such combinations exist, returns an empty list.
    """
    result = []

    freq_map = {}
    for num in nums_list:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    # Convert to list of (num, count) pairs
    unique_numbers = []
    for num in freq_map:
        unique_numbers.append((num, freq_map[num]))

    def backtrack(index, current, total):
        # Base case: valid combination
        if total == target_sum:
            result.append(current[:])
            return
        # Stop if total too big or out of bounds
        if total > target_sum or index >= len(unique_numbers):
            return

        num, max_count = unique_numbers[index]
        for count in range(max_count + 1):
            for _ in range(count):
                current.append(num)
            backtrack(index + 1, current, total + num * count)
            for _ in range(count):
                current.pop()  # Backtrack

    backtrack(0, [], 0)
    return result
