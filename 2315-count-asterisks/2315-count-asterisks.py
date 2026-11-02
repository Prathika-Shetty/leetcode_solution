class Solution:
    def countAsterisks(self, s: str) -> int:
        count=0
        pair=False
        for ch in s:
            if ch=='|':
                pair=not pair
            elif ch=='*' and pair==False:
                count+=1
        return count            