# Code written by Mohammad Mirmoosavi
# Problem link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Date: 2024-06-07

from typing import List


class Solution:

    @staticmethod
    def rec_count_negatives(grid: List[List[int]]) -> int:
        '''
        this recursive method counts negative numbers that exist in a two dimensional grid
        the algorithm : 1. you start from last row and first column
                        2. when you faced with a negative number, last row deleted and go up
                        3. when you faced with a positive number, first column deleted and go right

        :param grid: two dimensional arrays include non-increasing integers
        :return: the number of negative numbers that existed in sorted matrix
        '''
        # count of grid rows
        m = len(grid)

        # If grid has no rows, return 0
        if not m > 0:
            return 0
        # count of grid columns
        n = len(grid[0])

        # If grid has no columns, return 0
        if not n > 0:
            return 0

        # Start from the last row and the first column
        # If the element at (m-1, 0) is negative
        # while m and n > 0 we call recursive
        # O(n + m)
        if grid[m - 1][0] < 0:
            # Remove the last row and add the count of negative numbers in that row (which is n)
            # O(m)
            return Solution.rec_count_negatives(grid[:m - 1]) + n
        else:
            # If the element is non-negative, remove the first column from each row
            # O(n)
            return Solution.rec_count_negatives([sub_grid[1:] for sub_grid in grid])

    @staticmethod
    def non_rec_count_negatives(grid: List[List[int]]) -> int:
        '''
        this non recursive method counts negative numbers that exist in a two dimensional grid
        the algorithm : 1. you start from last row and first column
                        2. when you faced with a negative number, last row deleted and go up
                        3. when you faced with a positive number, first column deleted and go right

        :param grid: two dimensional arrays include non-increasing integers
        :return: the number of negative numbers that existed in sorted matrix
        '''
        negative_numbers = 0
        # count of grid rows
        m = len(grid)

        # count of grid columns

        n = len(grid[0])

        # while m and n > 0 we iterate over this functionality
        # O(n + m)
        while m > 0 and n > 0:
            if grid[m - 1][0] < 0:
                # O(m)
                negative_numbers += n
                m -= 1
                grid = grid[:m]
            else:
                # O(n)
                n -= 1
                grid = [sub_grid[1:] for sub_grid in grid]

        return negative_numbers


test_grid_case_1 = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
test_grid_case_2 = [[3, 2], [1, 0]]

negative_number_1 = Solution.rec_count_negatives(test_grid_case_1)
print(negative_number_1)

negative_number_2 = Solution.rec_count_negatives(test_grid_case_2)
print(negative_number_2)

negative_number_3 = Solution.non_rec_count_negatives(test_grid_case_1)
print(negative_number_3)

negative_number_4 = Solution.non_rec_count_negatives(test_grid_case_2)
print(negative_number_4)
