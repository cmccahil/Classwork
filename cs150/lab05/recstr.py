#recstr.py
#1.prompt the user for a string s
#2.prompt the user for string t,
#3.print s backwards
#4.print whether or not s is a palindrome,
#5.print whether t appears as a (possibly non-consecutive)subsequence of s.

def rev(s):
    if len(s)==0:
        return s
    else:
        return s[-1]+rev(s[0:len(s)-1])

def pal(s):
    if len(s)==0 or len(s)==1:
        return "is"
    if s[len(s)-1]==s[0]:
        return pal(s[1:len(s)-1])
    else:
        return "is not"

def subseq(s,t):
    if len(t)==0:
        return "is"
    if len(t)>len(s):
        return "is not"
    if s[0]==t[0]:
        return subseq(s[1:len(s)],t[1:len(s)])
    if s[0]!=t[0]:
        return subseq(s[1:len(s)],t)

def main():
    print("Welcome to my Incredible Recursive string thing!")
    print()
    s=input("Please enter a string s:")
    t=input("Please enter a string t:")
    print("The string \"",s,"\" backwards is \"",rev(s),"\".",sep='')
    print("The string \"",s,"\" ", pal(s), " a palindrome.",sep='')
    print("The string \"",t,"\" ",subseq(s,t)," a subsequence of \"",s,"\".",
          sep='')
main()
