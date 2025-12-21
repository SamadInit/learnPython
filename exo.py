def delDouble(s):
    b=""
    for i in range(len(s)-1):
        
        if s[i]!=s[i+1]:
            b=b+s[i]
    if b[-1]!=s[-1]:
     b=b+s[-1]   
    return b
        
def fusionLists(a,b):
   l=[]
   j=0
   for i in a:
      l.append(i)
      if j<len(b):
        l.append(b[j])
      j+=1
   return l

def reverseValKey(di):
   return { val:key for key,val in di.items()}

def fusionSameVal(d1,d2):
     for i in d2:
        if i in d1:
           d1[i]+=d2[i]
        else :
           d1[i]=d2[i]   
     return d1   
            
   


