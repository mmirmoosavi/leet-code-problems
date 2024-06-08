from typing import List, Dict


class Solution:

    @staticmethod
    def make_hashmap(nums: List[int], target) -> Dict:
        '''
        take a list of numbers and a target value and return hashmap with this structure:
        {
           target - num1 : index of num1 in array,
           target - num2 : index of num2 in array,
           .....
        }
        :param nums:
        :param target:
        :return: hashmap
        '''
        hashmap = dict()
        # create a hashmap from nums in O(n)
        for index, num in enumerate(nums):
            hashmap[target - num] = index

        return hashmap

    def twoSum(self, nums: List[int], target) -> List[int]:
        '''
        take a list of numbers and target value and return index of two numbers such that they add up to target value
        1. first take a hashmap with O(n) time complexity from the array
        2. iterate over array numbers if hashmap[number] is existed return the index of the number and index of the hashmap[number] (target - number)
        if there is no hashmap it shows that there is no two numbers that add up to target value and return -1
        :param nums:
        :param target:
        :return: index of two numbers such that they add up to target
        '''

        hashmap = self.make_hashmap(nums, target)

        for index, num in enumerate(nums):
            hashmap_index = hashmap.get(num, None)
            if hashmap_index:
                return [index, hashmap_index]
        return -1


sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 3], 6))
