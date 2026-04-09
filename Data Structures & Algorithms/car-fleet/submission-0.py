class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car cannot pass another car, can only catch up and drive same speed from there
        stack = []
        maps = {}
        fleet = 0
        for i in range(len(position)):
            time = (target-position[i]) / speed[i]
            stack.append([position[i], time])
        stack.sort()
        print(stack)
        curr = stack.pop()
        fleet +=1
        while stack:
            temp = stack.pop()
            if temp[1] > curr[1]:
                curr = temp
                fleet +=1
        return fleet




        