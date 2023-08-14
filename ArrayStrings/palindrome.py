class Palindrome:

    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join([char.lower() for char in s if char.isalpha() or char.isnumeric()])
        for i in range(int(len(new_string) / 2)):
            if new_string[i] != new_string[len(new_string) - i - 1]:
                return False

        return True

if __name__ == '__main__':
    print(Palindrome().isPalindrome("A man, a plan, a canal: Panama"))
    print(Palindrome().isPalindrome("0P"))


