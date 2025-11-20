def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    n=len(s)
    if n<2:
        return ""
    bs=0
    bl=0
    def expand(l,r):
        nonlocal bs,bl
        while l>=0 and r<n and s[l]==s[r]:
            cl=r-l+1
            if cl>bl and cl>=2:
                bs=l
                bl=cl
            l-=1
            r+=1
    for i in range(n):
        expand(i,i)
        expand(i,i+1)
    if bl<2:
        return ""
    return s[bs:bs+bl]
