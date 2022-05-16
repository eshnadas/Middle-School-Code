import time 

numbers = {}
def Fast_Fibonnaci(n):
    if n in numbers:
        return numbers[n]
    if n == 0 or n ==1:
        return 1
    else: 
        numbers [n] = Fast_Fibonnaci(n-2) + Fast_Fibonnaci(n-1) 
        return numbers [n]

starttime = time.time()        
print(Fast_Fibonnaci(100))
print(time.time() - starttime)

def Slow_Fibonnaci(n):
    if n == 0 or n ==1:
        return 1
    else: 
        return Slow_Fibonnaci(n-2) + Slow_Fibonnaci(n-1) 

starttime = time.time()       
print(Slow_Fibonnaci(100))
print(time.time() - starttime)