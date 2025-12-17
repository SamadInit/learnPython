
def mvSpaces(s):
    b=""
    c=""
    for k in range(len(s)):
        if s[k]!=" ":
            break
        else :
            b=s[k+1:]
            continue
    if b=="":
     b=s

    for i in range(len(b),0,-1):
         if b[i-1]!=" ":
                break
         else :
             c=b[:i-1]
             continue
    if c=="":
        c=b
    return c

def nmbrOfWords(s):
    n=1
    for i in range(len(s)) :
        if s[i]==" " and  s[i+1]!=" ":
            n+=1

    return n

def nbrOfVowels(s):
    n=0
    for i in s:
        if i =="a" or i=="e" or i=="i" or i=="u" or i=="o":
            n+=1
    return n 

def frequenceNote(l):
    b=[]
    s=0
    for i in l:
        if i[1] not in b:
            for j in l: 
                if i[1]==j[1]:
                 s+=1
        b.append((i[1],s))
        s=0
        
    return {i[0]:i[1] for i in b}

d=[("ahlam",19),("rachid",14),("ahmed",19),("mohammed",6),("abdessamad",19)]

print(frequenceNote(d))