class Solution:
    def countBits(self, n: int) -> List[int]:
        count_1s = []
        for i in range(n+1):
            count = 0
        # Brian Kernighan’s Algorithm (Optimal Loop)
            while i > 0:
                i &= (i - 1)  # Clears the rightmost '1' bit
                count += 1
            count_1s.append(count)
        return count_1s