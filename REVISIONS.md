Given that I was allowed to address the solution without a time limit, I took my time and tried to approach it methodically.

I first built up the structure of the class.  Next, added the test cases.  With these in place, I could check my work as I progressed and, though the test cases were limited, use a test driven approach to development.

I started by trying to solve one iteration and get the test cases matching, using a copy of the input state.  Herein is the "trick" to the problem.  We can't augment the state while reading it without throwing off our results.  We must therefore first create a copy to read from and write to another target.

Next, I added a recursive solution to allow for the 20th generation case.

Next, I moved from recursive to iterative, realizing that particularly by copying the board each iteration we were likely to reach memory limits at some point with a recursive solution.

Finally, I realized that we can further enhance the algorithm by altering the input in-place.  This is accompished by mapping the state transitions and using these temporary mappings during processing to keep track of both the prior and future state.  The state transitions were simple enough that this could be done in a relatively elagant way.  At the conclusion of the algorithm, we remap to the known input states.  The remapping step in the in-place solution has the same time cost as the copy step in the prior solution so we're able to keep time complexity the same while reducing space complexity.

If I had more time, I'd likely pull the test cases out of the Solution, into another file.  As is, the Solution is a bit verbose and the tests really don't belong coupled with the solution.
