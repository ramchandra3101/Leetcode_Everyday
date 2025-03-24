"""/*1. Same Substring
Two strings, 5, and t, each of length n, that contain lowercase English characters are given as well as an integer K.
• The cost to change the i character in s from s, to t, is the absolute difference of the ASClI value of characters, i.e., abs( s, - 4,).
Find the maximum length of a substring of s that can be changed to the corresponding substring of t with a total cost less than or equal to
K. If there is no such substring, return O.
Example
It is given that s = "adpgki", t = "cdmxki", K= 6.
• Change so from 'a' to 'c' with cost = abs('a* - c) = 2. String s is now
"cdpgki" and K = 6 - 2 = 4.
• Change s≥ from 'p' to 'm' with cost = abs(p' - 'm") = 3. String s is "cdmgki" and K = 4 - 3 = 1.
• The only character left to change is 'g' to 'x', which costs more than K.

The longest substring in s that is equal to the corresponding substring
in tis s{O, 2] = tO, 2].
Hence, the answer is 3.
Function Description
Complete the function sameSubstring in the editor below.
sameSubstring has the following parameters:
strings: the string to alter
String t: the string to match int K: the maximum sum of costs
Returns
int. the maximum length of a substring that can be obtained
Constraints
• 1 5 n≤2 x 105
• 0 ≤ K≤ 106
• Strings s and t contain lowercase English letters only.
sameSubstring has the following parameters:
strings: the string to alter string t: the string to match int K: the maximum sum of costs
Returns
int. the maximum length of a substring that can be obtained
Constraints
• 1sn≤2x 105
• 0≤ K≤ 106
• Strings sand t contain lowercase English letters only."""

def SameSubstring(s,t,k):
    left =0
    currentCost =0
    maxLen = 0
    for right in range(len(s)):
        currentCost += abs(ord(s[right]) - ord(t[right])) #calclulate current cost for each diiefernce using Sliding window
        while currentCost > k:
            currentCost -= abs(ord(s[left]) - ord(t[left])) #shrink the window from left
            left += 1
        maxLen = max(maxLen, right - left + 1) # Even if window shrinks we will still check the max length
    return maxLen


if __name__ == "__main__":
    s = input("Enter the string s: ")
    t = input("Enter the string t: ")
    k = int(input("Enter the value of k: "))
    result = SameSubstring(s, t, k)
    print(result)

    
    