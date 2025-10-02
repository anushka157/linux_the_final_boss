#Problem: Sliding Window Maximum
#Description

#Given an array nums and a window size k, find the maximum element in each sliding window of size k.

#Medium-level because it combines data structures and efficient window handling

#Naive solution is O(n*k), but efficient solution uses deque in O(n)




from collections import deque

def sliding_window_max(nums, k):
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1:
        return nums

    deq = deque()
    max_values = []

    for i in range(n):
        # remove indices outside the window
        while deq and deq[0] < i - k + 1:
            deq.popleft()
        # remove smaller values at the end
        while deq and nums[i] > nums[deq[-1]]:
            deq.pop()
        deq.append(i)
        if i >= k - 1:
            max_values.append(nums[deq[0]])
    return max_values

# ---------------- Example Usage ----------------
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print("Sliding window maximum:", sliding_window_max(nums, k))
