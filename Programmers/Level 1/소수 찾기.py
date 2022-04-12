def solution(n):
    sol = [True] * (n+1)
    
    for i in range(2,n+1):
        if sol[i] == True:
            for j in range(i+i,n+1,i):
                sol[j] = False
    
    return len([k for k in range(2,n+1) if sol[k]==True])