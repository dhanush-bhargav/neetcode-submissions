class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        optimal_k = max_k
        while min_k <= max_k:
            k = (max_k + min_k) // 2
            total_hours = 0
            for i in range(len(piles)):
                hours = piles[i] // k
                if piles[i] % k > 0:
                    hours+=1
                total_hours += hours
            if total_hours > h:
                min_k = k+1
            elif total_hours <= h:
                optimal_k = min(optimal_k, k)
                max_k = k-1
        return optimal_k
            
