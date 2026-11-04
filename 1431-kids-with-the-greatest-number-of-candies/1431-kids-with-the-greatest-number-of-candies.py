class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result=[]
        maxcandies=max(candies)
        for i in candies:
            if i+extraCandies>=maxcandies:
                result.append(True)
            else:
                result.append(False)
        return result