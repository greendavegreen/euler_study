def isPalindrome(item):
    """True if string is a palindrome

    ie. 303, 4004, 5445 all read the same from front to back and back to front.

    Parameters
    ----------
    item : str
        string for review
    Returns
    -------
    Boolean
        True if string is a palindrome
    """
    s = str(item)
    return s == s[::-1]


