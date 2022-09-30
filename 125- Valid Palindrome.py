def isPalindrome(s):
    TO_LOWER_CASE = 32
    ASCII_A = 65
    ASCII_Z = 90

    # remove non alphanumeric characters
    s = [cha for cha in s if (cha >= 'A' and cha <= 'Z') or (
        cha >= 'a' and cha <= 'z') or (cha >= '0' and cha <= '9')]

    # convert upper case to lower case
    for i in range(len(s)):
        if ord(s[i]) >= ASCII_A and ord(s[i]) <= ASCII_Z:
            s[i] = chr(ord(s[i]) + TO_LOWER_CASE)

    # check if palindrome string
    if len(s) % 2 == 0:
        if s[:len(s) // 2] == s[len(s):len(s) // 2 - 1:-1]:
            print('T')
            return True
        else:
            print('F')
            return False
    else:
        # exclude middle index character
        if s[:len(s) // 2] == s[len(s):len(s) // 2:-1]:
            print('T')
            return True
        else:
            print('F')
            return False


isPalindrome("A man, a plan, a canal: Panama")
