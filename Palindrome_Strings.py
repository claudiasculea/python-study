s = input("Write your sentence: ")

def isPalindrome(s):

    def toChars(s):
        s = s.lower() #method to convert characters to lower case
        ans = ""
        for i in s:  #string iteration
            if i in "qwertyuiopasdfghjklzxcvbnm":
                ans +=i
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1]) #slicing  first and last characters
    return isPal(toChars(s))
print("Is your sentence a palindrome?")
print(isPalindrome(s))
