Value Shuffling

Problem Statement

You are given three integers **A**, **B**, **C** and one string **S**. Your task is to swap the values among them in in the following sequence:

     A→B
     B→C
     C→A

After these swaps, the values of **A**, **B**, and **C** should be replaced accordingly.

Write a program that performs the specified swaps and outputs the values of **A**, **B**, and **C** in the given order in string **S**.

Input

Three integers **A**, **B**, and **C**, separated by spaces. Additionally, a string representing the order in which to show the values after performing the swap, consisting of three uppercase letters ('A', 'B', 'C'). The order string will not contain any spaces.

Output

After performing the swaps, print three integers in a single line representing the values of **A**, **B**, and **C** according to the given order. Separate the integers by spaces.

Constraints

     0≤A,B,C≤10000≤A,B,C≤1000

Example 1:

Input:

 5 10 15
 ABC

Output:

 15 5 10

Example 2:

Input:

 3 8 0
 BAC

Output:

 3 0 8 

Notes:

In second example, after swapping the values. A, B, and C becomes 0, 3 and 8. So, output is printed in the given order B(3) A(0) C(8).
