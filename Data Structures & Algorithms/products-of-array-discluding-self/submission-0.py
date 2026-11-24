class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        check_zero = defaultdict(int)
        product = 1
        res = []
        for n in nums:
            if n != 0:
                product *= n
            else:
                check_zero[0] += 1

        for n in nums:
            if len(check_zero) == 0:
                res.append(product // n)
            else:
                if n != 0:
                    res.append(0)
                else:
                    if check_zero[0] > 1:
                        res.append(0)
                    else:
                        res.append(product)
        return res