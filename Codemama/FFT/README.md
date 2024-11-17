FFT

Problem Statement

Full form of FFT is Fast Fourier transforms. Fast Fourier transforms are widely used for many applications in engineering, science, and mathematics. The basic ideas were popularized in 1965. In 1994, Gilbert Strang described the FFT as "the most important numerical algorithm of our lifetime". It is one of the complex algorithm to understand.

But today your tusk is a simple one. You are here to help litle Kana. Her teacher had given her a list of N strings and told her to find the full form of FFT. She doesn’t know the full form of FFT. So she decide to write down those consecutive strings which contain the first character ‘F’,‘F’,‘T’. As N can be very large so Kana hire you to write a program that will complete her tusk.

Input

A number NN and next NN line follows. Each line contains a string XiXi. It’s guaranteed that first character of each string is always ‘F’ or ‘T’.

Output

you have to print the total number of full forms (let it is V) in a single line. Then print V lines, the possible full forms of FFT. The strings should be separated by a blank space.

Constraints

    0≤N≤10000≤N≤1000
    1≤∣Xi∣≤101≤∣Xi∣≤10

Example 1:

Input:

7

Fast

Fourier

Transforms

Foo

Fnaarj

Fujura

Tanfu

Output:

2

Fast Fourier Transforms

Fnaarj Fujura Tanfu

Example 2:

Input:

5

Tasin

Fast

Tyll

Trrei

Fun

Output:

0

Notes:

In example 1, The strings "Fast", "Fourier", and "Transforms" form the full form of FFT. The strings "Fnaarj", "Fujura", and "Tanfu" also form the full form of FFT. Therefore, the output is 2, followed by the two full forms of FFT on two separate lines.
