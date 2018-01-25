def maxSubArray(lists):
    if not lists:
        return 0
    curSum = maxSum = lists[0]
    for i in lists[1:]:
        curSum = max(i, curSum + i)
        maxSum = max(maxSum, curSum)
    return maxSum