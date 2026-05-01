class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in hashMap:
                return [hashMap[complement] +1 ,i+1]
            hashMap[numbers[i]] = i
