#Print prime numbers from 1 to n natural numbers
#Find the frequency of each character in a string

def character_count(a):
    for char in set(a):
        print(f"Frequency of {char}:  ",a.count(char))
    
character_count("Rohan")

def prime_number(n):
    
    if n<2:
        print("give number greater than 2!!")
        return
    for num in range(2,n+1):
        test=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                test=False
                break
        if test:
            print(num)

prime_number(10)

    

    
    
