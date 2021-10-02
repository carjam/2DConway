#!/usr/bin/env python3
import sys
sys.path.append('./')
import utility

from typing import List

import numpy as np

class Solution:
    def __init__(self):
        pass

    def populationAfterNDays(self, cells: List[List[int]], N: int) -> List[List[int]]:
        return cells

    def validate(self, case1: List[List[int]], case2: List[List[int]]) -> List[List[int]]:
        m1, m2 = len(case1), len(case2)
        if m1 < 1 or m2 < 1:
            return None 
        n1, n2 = len(case1[0]), len(case2[0])
        if n1 < 1 or n2 < 1:
            return None
        if m1 != m2 or n1 != n2:
            return None
           
        res = [row[:] for row in case1]
        for i, v1 in enumerate(case1):
            for j, v2 in enumerate(case2):
                if case1[i][j] == case2[i][j]:
                    res[i][j] = 'O'
                else:
                    res[i][j] = 'X'
        return res

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
        print("\n\ntest1:\nstart:\n")
        print(np.matrix(start1))
        print("\nend:\n")
        print(np.matrix(end1))
        print("\nmatch\n")
        print(np.matrix(match))
        #assert(match == end1)
    
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
        print("\n\ntest2:\nstart:\n")
        print(np.matrix(start2))
        print("\nend:\n")
        print(np.matrix(end2))
        print("\nmatch\n")
        print(np.matrix(match))
        #assert(match == end2)
    
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
        print("\n\ntest3:\nstart:\n")
        print(np.matrix(start3))
        print("\nend:\n")
        print(np.matrix(end3))
        print("\nmatch\n")
        print(np.matrix(match))
        #assert(match == end3)

@utility.profile
def main():
    solution = Solution()
    solution.test1()
    solution.test2()
    solution.test3()
    twenty = solution.run()
    print("\n20:\n",np.matrix(twenty))
    
if __name__ == "__main__":
    main()
