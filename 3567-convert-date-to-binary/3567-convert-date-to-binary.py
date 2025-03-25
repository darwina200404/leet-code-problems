class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        Bin_date=date.split('-')
        ans=[]
        for val in Bin_date:
            ans.append(bin(int(val))[2:])
        return '-'.join(ans)

        
        