class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        text_vowels = []
        new_text = []
        for letter in s:
            if letter in vowels:
                text_vowels.append(letter)
        for letter in s:
            if letter in vowels:
               new_text.append(text_vowels.pop())
            else:
                new_text.append(letter)
        return "".join(new_text)



