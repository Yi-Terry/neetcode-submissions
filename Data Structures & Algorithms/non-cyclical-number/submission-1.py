class Solution:
    
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.square_sum(n)
        return True
        

    def square_sum(self, n):
        total = 0
        for num in str(n):
            total += int(num)**2
        return total