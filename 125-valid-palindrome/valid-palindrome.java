class Solution {
        public boolean check(int left, int right, String s) {
            
        if (left >= right)
            return true;

        if (!Character.isLetterOrDigit(s.charAt(left)))
            return check(left + 1, right, s);

        if (!Character.isLetterOrDigit(s.charAt(right)))
            return check(left, right - 1, s);

        if (Character.toLowerCase(s.charAt(left))
                != Character.toLowerCase(s.charAt(right)))
            return false;

        return check(left + 1, right - 1, s);
    }
    public boolean isPalindrome(String s) {
        return check(0, s.length() - 1, s);
        
    }
}