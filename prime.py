n=int(input("Enter ending limit of range: "))

prime_number=set(range(2,n+1))

while prime_number:
    
    prime=min(prime_number)
    
    print(prime,end="\n")
    
    prime_number-=set(range(prime,n+1,prime))
 
    print()
