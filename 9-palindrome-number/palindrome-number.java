class Solution {
    public boolean isPalindrome(int x) {
        String a=String.valueOf(x);
        StringBuilder sb= new StringBuilder(a);
        String palindrome=sb.reverse().toString();
        if(a.equals(palindrome))
            return true;
        else
            return false;
    }

}

