#Author: Jesus Arias
#GitHub username: ariasje1
#Date: 08/01/2025
#Description: Gives unique combinations that sum to target value
def combination_sum(candidates, target):
    """
    Finds all unique combinations of numbers that sum up to 'target'.

    Parameters:
        candidates (List[int]): A list of distinct positive integers.
        target (int): The target sum to achieve.

    Returns:
        List[List[int]]: A list of all unique combinations where the chosen numbers sum to 'target'.
                         Each combination is a list of integers in non-decreasing order.
    """
    result = []

    def dfs(index, current, total):
        # Base case: found valid combination
        if total == target:
            result.append(current[:])
            return

        # Invalid case: out of bounds or sum too big
        if index >= len(candidates) or total > target:
            return

        # Choice 1: include candidates[index]
        current.append(candidates[index])
        dfs(index, current, total + candidates[index])  # reuse allowed

        # Backtrack and try next candidate
        current.pop()
        dfs(index + 1, current, total)

    dfs(0, [], 0)
    return result
