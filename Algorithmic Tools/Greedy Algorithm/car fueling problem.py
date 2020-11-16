x=[0,200,375,550,750,950]
L=400
n=4
def min_rifills(x,n,L):
    current_rifill=0
    number_rifill=0
    while(current_rifill<=n):
        lastrifill=current_rifill
        while(current_rifill<=n and (x[current_rifill+1]-x[lastrifill])<=L):
            current_rifill=current_rifill+1
        
        if current_rifill==lastrifill:
            return False
        if current_rifill<=n:
            number_rifill+=1
            
    return number_rifill
    
    
print(min_rifills(x,n,L))