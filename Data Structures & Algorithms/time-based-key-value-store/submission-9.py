class TimeMap:

    def __init__(self):
        self.maps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.maps:
            self.maps[key] = []
        self.maps[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.maps:
            return ""
        vals = self.maps[key]
        l = 0
        r = len(vals)-1
        mininum = ""
        while l <=r :
            mid = (l+r)//2
            if vals[mid][0] == timestamp:
                return vals[mid][1]
            elif vals[mid][0] < timestamp:
                l = mid+1
                mininum = vals[mid][1]
            else:
                r = mid-1
        return mininum
