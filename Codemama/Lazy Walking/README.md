Lazy Walking

Problem Statement

For being lazy you are punished to walk on the garden at least NN steps. As you mastered laziness, after ithith step you take rest for ii second(s). You also takes X second(s) to complete each step. Now write a program to calculate the total time to take exactly NN steps.

Input

One line contains two integer NN and XX.

Output

You have to print total time needed to take exactly NN steps in a single line.

Constraints

    1≤N≤100001≤N≤10000
    0≤X≤100≤X≤10

Example 1:

Input:

5 2

Output:

20

Example 2:

Input:

3 1

Output:

6

Notes:

In example 2, you need to walk 3 steps. After first step, you take rest for 1 second. After second step you take rest for 2 seconds. You also takes 1 second to complete each step. Therefore, the total time to take exactly 3 steps is (1 + 2)(resting time) + (3 * 1)(stepping time) = 6 seconds.
