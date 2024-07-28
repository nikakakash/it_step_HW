def reverse_string(s):
    return s[::-1]
class func:


    def is_palindrome(self,s):
        return s == s[::-1]

    def capitalize_words(self,s):
        return ' '.join(word.capitalize() for word in s.split())

    def celsius_to_fahrenheit(self,c):
        return c * 9 / 5 + 32

    def fahrenheit_to_celsius(self,f):
        return (f - 32) * 5 / 9


f=func()
print(f.capitalize_words('aaa'))