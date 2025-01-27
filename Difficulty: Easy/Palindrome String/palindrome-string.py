#User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_string=s[::-1]
        if(s==reverse_string):
            return True
        else:
            return False


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()  # Use lowercase 's'
        ob = Solution()
        answer = ob.isPalindrome(s)
        print("true" if answer else "false")  # Print "true" or "false"
        print("~")

# } Driver Code Ends