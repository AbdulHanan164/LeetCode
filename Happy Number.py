class Solution {
public:
    // Function to calculate the sum of squares of digits
    int digitSquareSum(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
    
    bool isHappy(int n) {
        int slow = n;
        int fast = n;
        
        do {
            slow = digitSquareSum(slow);          // Move slow one step
            fast = digitSquareSum(fast);          // Move fast two steps
            fast = digitSquareSum(fast);          // Move fast again
        } while (slow != fast);                   // Stop when slow equals fast
        
        return slow == 1;  // If we reached 1, it's a happy number; otherwise, it's not
    }
};
