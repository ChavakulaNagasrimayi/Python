l=[7,8,9,10]
def sumsquare(l):
    even=0
    odd=0
    for i in l:   
       if i%2==0:
        even=even+i**2
       else:
        odd=odd+i**2
    l=[odd,even]
    return(l)
print(sumsquare(l))
