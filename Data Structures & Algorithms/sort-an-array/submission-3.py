class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr):
            def merge(left, right):
                res = []
                while left and right:
                    if left[0] < right[0]:
                        res.append(left.pop(0))
                    else:
                        res.append(right.pop(0))
                while left:
                    res.append(left.pop(0))
                while right:
                    res.append(right.pop(0))
                return res

            if len(arr) <= 1:
                return arr
            left = mergesort(arr[len(arr)//2:])
            right = mergesort(arr[:len(arr)//2])
            return merge(left, right)

        return mergesort(nums)

        