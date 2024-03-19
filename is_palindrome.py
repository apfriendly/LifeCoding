def is_palindrome(x: int) -> bool:

    digits = [i for i in str(x)]
    if digits == digits[::-1]:
        return True
    return False


print(is_palindrome(10))
