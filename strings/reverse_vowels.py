class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowel_string = ''
        vowel_indices = []
        
        vowels = {}
        for vowel in 'aeiouAEIOU':
            vowels[vowel] = 1
            
    
        for index, letter in enumerate(s):
            if letter in vowels:
                vowel_string += letter
                vowel_indices.append(index)
                
                
        reversed_vowels = vowel_string[::-1]
        
        output = ['']*len(s)
        l = 0
        for i in range(len(s)):
            if s[i] in vowels:
                output[i] = reversed_vowels[l]
                l += 1
            else:
                output[i] = s[i]
                
        return ''.join(output)
