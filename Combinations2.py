'''
Given a collection of candidate numbers (candidates) and a target number (target)
Find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''

def combinationSum2(candidates, target):
    candidates.sort()
    result = []
    helper(candidates, 0, [], result, target)
    return result


def helper(candidates, start, path, result, target):
    if not target:
        result.append(path)
        return

    for i in range(start, len(candidates)):
        # Ignore duplicates
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        # If current element is greater than target break
        if candidates[i] > target:
            break
        helper(candidates, i + 1, path + [candidates[i]], result, target - candidates[i])

if __name__ == '__main__':
    A = [10,1,2,7,6,1,5]
    target = 8
    print(combinationSum2(A, target))
    # Result : [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]