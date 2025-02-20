'''A squared string is a string of n lines, 
each substring being n characters long. 
We are given two n-squared strings.

For example:

s1 = "abcd\nefgh\nijkl\nmnop"

s2 = "qrst\nuvwx\nyz12\n3456"

Let us build a new string strng of size (n + 1) x n
 in the following way:

The first line of strng has the first char of the 
first line of s1 plus the chars of the last line 
of s2.
The second line of strng has the first two chars 
of the second line of s1 plus the chars of the 
penultimate line of s2 except the last char
and so on until the nth line of strng has the n 
chars of the nth line of s1 plus the first char 
of the first line of s2.
'''
# my solution

def compose(s1, s2):
    s1_lines = s1.split('\n')
    s2_lines = s2.split('\n')
    s3_lines = []
    for i in range(len(s1_lines)):
        part1 = s1_lines[i][:i+1]
        part2 = s2_lines[-(i+1)][:len(s1_lines)-i]
        new_line = part1 + part2
        s3_lines.append(new_line)
    result = '\n'.join(s3_lines)
    return result