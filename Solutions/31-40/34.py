import math 
  
def CheckPrime(n): 
    if n <= 1: 
        return False
      
    if n == 2: 
        return True
          
    if n%2 == 0: 
        return False
          
    for i in range(3, int(math.sqrt(n))+1, 2): 
        if n%i == 0: 
            return False
    return True
  

def isPossible(n): 

    if CheckPrime(n) and CheckPrime(n - 2): 
        return True
    else: 
        return False
  

n = 13
if isPossible(n) == True: 
    print("Yes") 
else: 
    print("No") 