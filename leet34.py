class Solution:
    def binary_search(self, lo, hi, condition):
        while lo <= hi:
            mid = (lo + hi) // 2
            result = condition(mid)
            # print(result)
            if result == "right":
                lo = mid + 1
            elif result == "left":
                hi = mid - 1
            else:
                return result
        return [-1, -1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, 0

        def condition(mid):
            mid_num = nums[mid]
            if mid_num == target:
                start = mid
                end = mid
                while start - 1 >= 0 and nums[start - 1] == target:
                    start -= 1
                while end + 1 < len(nums) and nums[end + 1] == target:
                    end += 1
                return [start, end]
            elif mid_num <= target:
                result = "right"
            else:
                result = "left"
            return result

        return self.binary_search(0, len(nums) - 1, condition)

