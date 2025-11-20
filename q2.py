def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    while True:
        ns=""
        i=0
        chn=False
        while i<len(s):
            if i+1<len(s) and s[i]==s[i+1]:
                ch=s[i]
                chn=True
                while i<len(s) and s[i]==ch:
                    i+=1
            else:
                ns+=s[i]
                i+=1
        if not chn:
            return ns
        s=ns
