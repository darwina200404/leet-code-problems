class Solution {
public:
    bool isPalindrome(int x) {
        int temp=x;
        int rev=0;
        while(x>0){
            int las=x%10;
            if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && las > 7)) return 0;
            if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && las < -8)) return 0;
            rev=rev*10+las;
            x=x/10;

        }
        return(rev==temp);
        
    }
};