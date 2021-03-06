"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""

J = "aA"
S = "aAAbbbb"

def num_jewels_in_stones(jewels, stones):
    """ Takes in jewel indentifier(s) & list of stones. Returns integer of how many jewels are in the stones. """
    stones_dictionary = {}
    num_of_jewels = 0
    for stone in stones:
        stones_dictionary[stone] = stones_dictionary.get(stone, 0)+1
    for jewel in jewels:
        num_of_jewels += stones_dictionary.get(jewel,0)
    return num_of_jewels
        
num_jewels_in_stones(J,S)