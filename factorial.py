#Factorial of number

fact = 1
num = int(input("Enter number to calculate factorial: "))

while(num>0):
    fact = fact * num
    num-=1
print(f"Factorial is {fact}")
