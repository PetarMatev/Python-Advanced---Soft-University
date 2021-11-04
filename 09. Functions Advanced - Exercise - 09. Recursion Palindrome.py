# 09. Recursion Palindrome:
def palindrome(word, index=0, result="", constant=None):
    if constant is None:
        constant = word
    if len(word) == index:
        if result == constant:
            return f"{constant} is a palindrome"
        return f"{constant} is not a palindrome"

    last_letter = word[len(word) - 1]
    result += last_letter
    return palindrome(word=word[:-1], index=index, result=result, constant=constant)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
