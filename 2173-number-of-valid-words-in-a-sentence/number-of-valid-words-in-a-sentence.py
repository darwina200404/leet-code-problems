class Solution(object):
    def ValidWord(self,token):
        punctuation_marks = set("!.,")
        if any(ch.isdigit() for ch in token):
            return False
        if token.count('-') > 1:
            return False
        if '-' in token:
            idx = token.find('-')
            if idx == 0 or idx == len(token) - 1:
                return False
            if not (token[idx - 1].islower() and token[idx + 1].islower()):
                return False
        punctuation_count = sum(1 for ch in token if ch in punctuation_marks)
        if punctuation_count > 1:
            return False
        if punctuation_count == 1:
            if token[-1] not in punctuation_marks:
                return False
            if any(ch in punctuation_marks for ch in token[:-1]):
                return False
        for ch in token:
            if not (ch.islower() or ch in "-!.,"):
                return False

        return True
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        count=0
        words=[word for word in sentence.split() if word]
        for i in words:
            if self.ValidWord(i):
                count+=1
        return count

            
        