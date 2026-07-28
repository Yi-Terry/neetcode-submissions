class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = stones[:]

        while len(stones) > 1:
            stones.sort()
            y = stones.pop() #first largest
            x = stones.pop() # second largest
            if y != x:
                stones.append(y-x)
        return stones[0] if stones else 0