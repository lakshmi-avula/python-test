"""
given string is palindrome or not
write a function for palindrome

def is_palindrome(string):
    logic
    :return: yes or no

case1: abcba -> yes
case2: aaaa  -> yes
case3: abc   -> no


procedure:
step1: take input from user
step2: pass through into the function
step3: process result
    3.1:
"""


# def is_palindrome(string):
#     return string == string[::-1]
#
#
# input_string = input()
# print(is_palindrome(input_string))


def is_palindrome(string1):
    if string1 == ''.join(reversed(string1)):
        return "yes"
    return "no"


string = input()
ans = is_palindrome(string)
print(ans)
