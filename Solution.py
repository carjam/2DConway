#!/usr/bin/env python3
import sys
sys.path.append('./')
import utility

import numpy as np

from typing import List
from collections import defaultdict


class Solution:

    def __init__(self):
        pass

    def populationAfterNDays(self, cells: List[List[int]], N: int) -> List[List[int]]:
        EMPTY = 0
        NEWB = 1
        ADULT = 2
        SENIOR = 3

        #EMPTY
        def passTimeEmpty(neibCnt):
            if neibCnt[ADULT] == 2: #reproduction
                return NEWB
            else: #no change
                return EMPTY
 
        #NEWB
        def passTimeNewb(neibCnt):
            total = sum(neibCnt[k] for k in neibCnt if k > EMPTY)
            if total >= 5: #overcrowding
                return EMPTY
            elif total <= 1: #isolation
                return EMPTY
            else: #growing up
                return ADULT

        #ADULT
        def passTimeAdult(neibCnt):
            total = sum(neibCnt[k] for k in neibCnt if k > EMPTY)
            if total >= 3: #overcrowding
                return EMPTY
            elif total <= 0: #isolation
                return EMPTY
            else: #aging
                return SENIOR

        #SENIOR
        def passTimeSenior(neibCnt):
            return EMPTY #natural causes

        def countNeighbors(cntCells, r, rows, c, cols):
            neibs = defaultdict(int)

            neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            for neighbor in neighbors:
                row, col = r + neighbor[0], c + neighbor[1]
                if row >= 0 and row < rows and col >= 0 and col < cols:
                    neibs[cntCells[row][col]] += 1

            return neibs

        ##
        if N <= 0:
            return cells
        rows = len(cells)
        cols = len(cells[0])
       
        copyCells = [[cells[row][col] for col in range(cols)] for row in range(rows)]

        for row in range(rows):
            for col in range(cols):
                nei = countNeighbors(copyCells, row, rows, col, cols)

                newVal = -1
                if copyCells[row][col] == EMPTY:
                    newVal = passTimeEmpty(nei)
                elif copyCells[row][col] == NEWB:
                    newVal = passTimeNewb(nei)
                elif copyCells[row][col] == ADULT:
                    newVal = passTimeAdult(nei)
                elif copyCells[row][col] == SENIOR:
                    newVal = passTimeSenior(nei)

                #print(row, col, cells[row][col], newVal, nei)
                cells[row][col] = newVal

        return self.populationAfterNDays(cells, N-1)




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
        print("\n\ntest1:\nstart:\n")
        print(np.matrix(start1))

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
        print("\nend:\n")
        print(np.matrix(end1))
       
        res = self.populationAfterNDays(start1, 1)
        print("\nresult:\n")
        print(np.matrix(res))

        match = self.validate(res, end1);
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
        print("\n\ntest2:\nstart:\n")
        print(np.matrix(start2))

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
        print("\nend:\n")
        print(np.matrix(end2))

        res = self.populationAfterNDays(start2, 1)
        print("\nresult:\n")
        print(np.matrix(res))

        match = self.validate(res, end2)
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
        print("\n\ntest3:\nstart:\n")
        print(np.matrix(start3))

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
        print("\nend:\n")
        print(np.matrix(end3))
        
        res = self.populationAfterNDays(start3, 1)
        print("\nresult:\n")
        print(np.matrix(res))

        match = self.validate(res, end3)
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
