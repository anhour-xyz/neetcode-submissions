class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map[key]
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l+r) // 2
            if mid + 1 == timestamp:
                return arr[mid]
            elif mid < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return arr[mid]

            
