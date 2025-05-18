class Solution(object):
    def sumNumbers(self,num):
        sum=0
        while(num>0):
            digit=num%10
            sum+=digit
            num=num/10
        return sum
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(num>9):
            num=self.sumNumbers(num)
        return num

        