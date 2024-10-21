242. Valid Anagram

Given two strings **s** and **t**, return true if **t** is annanagram of **s**, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

Personal Notes:

what is anagram?

- if a word has exactly same length as another word, and in whatever sequence contains exactly the same amount of letters as the other word, then the word is called an anagram of the said word.

In this solution, at first i'm checking if the words are same in length. If they are, I'm proceeding to check if the amount of each letters are same in both words.
For that, I'm creating two dictionaries where the letters will be *keys* and their occurances will be *values*. After populating the dictionaries using for loop, I'm comparing the *keys* of two words against their *values*.
