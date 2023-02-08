N = int(input())                       
                                       
n = list(map(int, input().split()))    
a = len(n)                             
                                       
for i in range(a-1):                   
    min_ = i                           
    for j in range(i+1, a):            
        if n[min_] > n[j]:             
            min_ = j                   
    n[i], n[min_] = n[min_], n[i]      
                                       
if N % 2 == 0:                         
    print(n[0] * n[-1])                
else:                                  
    print(n[a // 2] ** 2)              