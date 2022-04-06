"""
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.

 

Constraints:

    3 <= arr.length <= 3000
    0 <= arr[i] <= 100
    0 <= target <= 300


"""
# -NOTE: The following solution resutls in excessive runtime.
from itertools import combinations
class Solution:
    def threeSumMulti(self, arr: List[int], target : int) -> int:
        
        MOD = 10**9 + 7
        comb = combinations(arr, 3)
        count = 0
        
        for i in list(comb):
            if sum(i) == target:
                count += 1

        count %= MOD
        return count


# NOTE: Solution by LeetCode. Using 2-pointers.
"""
class Solution:
    def threeSumMulti(self, arr: List[int], target : int) -> int:
        MOD = 10**9 + 7
        ans = 0
        A = arr
        A.sort()

        for i, x in enumerate(A):
            # We'll try to find the number of i < j < k
            # with A[j] + A[k] == T, where T = target - A[i].

            # The below is a "two sum with multiplicity".
            T = target - A[i]
            j, k = i+1, len(A) - 1

            while j < k:
                # These steps proceed as in a typical two-sum.
                if A[j] + A[k] < T:
                    j += 1
                elif A[j] + A[k] > T:
                    k -= 1
                # These steps differ:
                elif A[j] != A[k]: # We have A[j] + A[k] == T.
                    # Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
                    # And similarly for "right".
                    left = right = 1
                    while j + 1 < k and A[j] == A[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and A[k] == A[k-1]:
                        right += 1
                        k -= 1

                    # We contributed left * right many pairs.
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1

                else:
                    # M = k - j + 1
                    # We contributed M * (M-1) / 2 pairs.
                    ans += (k-j+1) * (k-j) / 2
                    ans %= MOD
                    break

        return ans
"""