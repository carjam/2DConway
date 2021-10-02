#!/usr/bin/env python3
import sys
sys.path.append('./')
import utility

from typing import List

class Solution:
    def __init__(self):
        pass

    def populationAfterNDays(self, cells: List[List[int]], N: int) -> List[List[int]]:
        pass 

    def validate(self, case1: List[List[int]], case2: List[List[int]]) -> List[List[int]]:
        pass
    ###
    # General Coding Exercise Test Cases
    def run(self): 
        ## Final Problem Initial Data:
        start =  [
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,1,1,0,0,0,0,0,0],
           [0,0,0,0,2,0,0,0,0,0],
           [0,0,0,1,2,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,1,0,0,0,0,0,0,0],
           [0,2,1,0,0,0,0,0,0,0],
           [0,2,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
         ]
        res = self.populationAfterNDays(start, 20)
        return res


    ## Test Case 1:
    def test1(self):
        start1 = [
          [0,0,2,2,0,0,0,0,0,0],
          [0,0,0,0,1,3,1,0,0,0],
          [0,0,0,2,0,3,0,0,1,3],
          [0,0,0,0,1,3,0,0,0,3],
          [0,2,2,0,0,0,1,3,1,0],
          [0,0,0,0,0,2,2,0,0,0],
          [0,0,2,0,2,0,0,0,0,0],
          [0,0,0,0,2,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
        ]
        res = self.populationAfterNDays(start1, 1)
        print(res)

        #becomes (after 1 evolution)
        end1 = [
          [0,0,3,3,0,0,0,0,0,0],
          [0,0,0,0,2,0,2,0,0,0],
          [0,0,0,3,0,0,0,0,2,0],
          [0,1,0,1,2,0,0,0,0,0],
          [0,3,3,0,0,1,2,0,2,0],
          [0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,3,0,1,0,0,0],
          [0,0,0,0,3,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
        ]
        match = self.validate(res, end1);
        print("\n\ntest1:\nstart:\n", start1, "\nend:\n", end1, "\nmatch\n", match)
    
    ## Test Case 2:
    def test2(self):
        start2 = [
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,1,1,0,0,2,0,0,0],
          [0,0,3,3,2,0,0,0,2,0],
          [0,1,0,0,0,0,0,0,2,0],
          [0,0,3,0,0,1,2,0,0,0],
          [0,0,1,3,3,3,0,0,0,0],
          [0,0,0,1,0,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
        ]
        res = self.populationAfterNDays(start2, 1)

        #becomes (after 1 evolution)
        end2 = [
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,2,2,0,1,0,1,0,0],
          [0,0,0,0,3,1,0,0,3,1],
          [0,2,0,0,0,1,0,0,3,1],
          [0,0,0,0,0,2,3,1,0,0],
          [0,0,2,0,0,0,0,0,0,0],
          [0,0,0,2,0,2,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
        ]
        match = self.validate(res, end2)
        print("\n\ntest2:\nstart:\n", start2, "\nend:\n", end2, "\nmatch\n", match)
    
    ## Test Case 3:
    def test3(self):
        start3 = [
          [0,0,0,0,1,3,1,0,0,0],
          [0,0,0,0,0,3,0,0,0,0],
          [0,0,2,0,0,0,0,3,1,0],
          [0,0,2,0,2,3,0,0,3,0],
          [0,0,2,0,0,0,0,3,0,0],
          [0,0,0,0,0,2,1,3,1,0],
          [0,0,0,0,2,2,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
        ]
        res = self.populationAfterNDays(start3, 1)

        #becomes (after 1 evolution)
        end3 = [
          [0,0,0,0,2,0,2,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,1,3,0,0,0,0,0,2,0],
          [0,0,3,0,3,0,0,0,0,0],
          [0,1,3,0,1,1,0,0,0,0],
          [0,0,0,1,0,0,2,0,2,0],
          [0,0,0,0,3,0,1,0,0,0],
          [0,0,0,0,1,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
        ]
        match = self.validate(res, end3)
        print("\n\ntest3:\nstart:\n", start3, "\nend:\n", end3, "\nmatch\n", match)

@utility.profile
def main():
    solution = Solution()
    solution.test1()
    solution.test2()
    solution.test3()
    twenty = solution.run()
    print("\n20:\n",twenty)
    
if __name__ == "__main__":
    main()
