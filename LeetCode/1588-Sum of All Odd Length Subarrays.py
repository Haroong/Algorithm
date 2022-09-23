class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        answer = 0
        sumOfSubarray = []

        # check odd length subarray
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr) + 1):
                if len(arr[j:j + i]) != i:
                    break

                temp = sum(arr[j:j + i])
                sumOfSubarray.append(temp)

        # sum of all each steps
        answer = sum(sumOfSubarray)

        return answer

        
