from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_length = float("inf")
        window_start = window_end = 0
        bit_counts = [0] * 32  # Tracks count of set bits at each position

        # Expand window until end of array
        while window_end < len(nums):
            # Add current number to window
            self._update_bit_counts(bit_counts, nums[window_end], 1)

            # Contract window while OR value is valid
            while (
                window_start <= window_end
                and self._convert_bits_to_num(bit_counts) >= k
            ):
                # Update minimum length found so far
                min_length = min(min_length, window_end - window_start + 1)

                # Remove leftmost number and shrink window
                self._update_bit_counts(bit_counts, nums[window_start], -1)
                window_start += 1

            window_end += 1

        return -1 if min_length == float("inf") else min_length

    def _update_bit_counts(
        self, bit_counts: list, number: int, delta: int
    ) -> None:
        # Update counts for each set bit in the number
        for pos in range(32):
            if number & (1 << pos):
                bit_counts[pos] += delta

    def _convert_bits_to_num(self, bit_counts: list) -> int:
        # Convert bit counts to number using OR operation
        result = 0
        for pos in range(32):
            if bit_counts[pos]:
                result |= 1 << pos
        return result

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))