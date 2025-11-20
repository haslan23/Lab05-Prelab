def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    a=a[2:]
    b=b[2:]
    i=len(a)-1
    j=len(b)-1
    cr=0
    rl=""
    while i>=0 or j>=0 or cr:
        ba=ord(a[i])-ord('0') if i>=0 else 0
        bb=ord(b[j])-ord('0') if j>=0 else 0
        tt=ba+bb+cr
        rl=str(tt % 2)+rl
        cr=tt//2
        i-=1
        j-=1
    k = 0
    while k<len(rl)-1 and rl[k]=='0':
        k+=1
    rl=rl[k:]
    return "0b"+rl
