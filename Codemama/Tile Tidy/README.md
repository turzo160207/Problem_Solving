Tile Tidy

Problem Statement

There are **N** tiles in a row with red, green or blue paint. How many tiles do you need to remove so that no two consecutive tiles have the same color? Consecutive tiles are those that are next to each other.

Input

The first line contains integer **N** the number of tiles.

The next line contains string **S**, which represents the colors of the tiles. The i-th character of **S** equals "R", if the i-th tile is red, "G", if it's green and "B", if it's blue.

Output


Print a single integer, the number of tiles needed to be removed.

Constraints

    1≤N≤100

Example 1:

Input:

2

RG

Output:

0

Example 2:

Input:

3

BBB

Output:

2

Notes:

In example 2, we have 3 tiles, all of which are blue. We need to remove 2 tiles to ensure that no two consecutive tiles have the same color.
