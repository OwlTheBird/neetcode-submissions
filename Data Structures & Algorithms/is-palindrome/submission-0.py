class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())

        s_list = list(s)

        rev_s_list = list(reversed(s_list.copy()))

        for i in range(len(s_list)):
            if s_list[i] != rev_s_list[i]:
                return False

        return True

        