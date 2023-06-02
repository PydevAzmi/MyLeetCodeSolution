class Solution(object):

    def split_integer(self, an_int):
        x = math.log(an_int, 10)
        y = int(math.ceil(x))

        return [(an_int//(10**i)) % 10 for i in range(y, -1, -1)][bool(math.log(an_int, 10) % 1):]

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0 :
            return True
        elif x > 0:
            current_list = self.split_integer(x)
            inverse_list = current_list[::-1]
            if inverse_list == current_list:
                is_palindrome = True
            else:
                is_palindrome = False
        else :
            is_palindrome = False

        return is_palindrome