class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """


        #separate string and num characters
        alphs = []
        digits = []
        for let in s:
            if let.isalpha():
                alphs.append(let)
            elif let.isnumeric():
                digits.append(let)

        if len(alphs) == 1 and len(digits) == 0:
            return s
        
        if (len(digits)) == 1 and len(alphs) == 0:
            return s

        if len(alphs) == len(s):
            return ""

        if len(digits) == len(s):
            return ""


        total = len(alphs) + len(digits)
        output = ''

        if len(alphs) - len(digits) == 1:
            output += alphs.pop()
            while len(digits) > 0:
                output += digits.pop()
                output += alphs.pop()


        elif len(digits) - len(alphs) == 1:
            output += digits.pop()
            while len(alphs) > 0:
                output += alphs.pop()
                output += digits.pop()

        elif len(digits) - len(alphs) == 0:
            while len(alphs) > 0:
                output += digits.pop()
                output += alphs.pop()

        else: 
            return ""

        return output
        
