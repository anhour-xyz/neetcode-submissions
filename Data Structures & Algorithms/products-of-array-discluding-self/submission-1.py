class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        map = defaultdict(int)
        product = 1
        for n in nums:
            if n != 0:
                product *= n
            else:
                map[0] += 1
        
        res = []
        for n in nums:
            if n != 0:
                if map[0] == 0:
                    res.append(product // n)
                else:
                    res.append(0)
            else:
                if map[0] == 1: res.append(product)
                else: res.append(0)
        return res