class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        boats = 0
        while l<=r:
            if l == r:
                boats += 1
                l += 1
                break
            remainder = limit - people[r]
            r-=1
            if people[l] <= remainder:
                l+=1
            boats+=1
        return boats
        