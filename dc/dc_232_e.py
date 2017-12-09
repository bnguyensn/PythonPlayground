# Daily Challenge #232 [Easy]: Palindrome

# Key takeaways:
# punctuation list, remove punctuations
# maketrans()
# reverse a string

from string import punctuation

inp = 'Was it a car or a cat I saw?'


def palindrome_check(s):
    s_ltr = ''.join(s.translate(str.maketrans('', '', punctuation)).split()).lower()
    s_rtl = s_ltr[::-1]
    return s_ltr == s_rtl


if palindrome_check(inp):
    print('Input is a palindrome.')
else:
    print('Input is NOT a palindrome.')
