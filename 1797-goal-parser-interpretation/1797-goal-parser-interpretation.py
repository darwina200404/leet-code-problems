class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans=""
        for i in range (len(command)):
            if (command[i].isalpha()):
                ans+=command[i]
            elif (command[i] == '(' and command[i+1]==')' ):
                ans+="o"
        return ans;

