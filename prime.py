num = int(input("Enter number to check if it is prime or not: "))

if num>1:
    for i in range(2, int(num/2)+1):
        if(num%i)==0:
            print(f"{num} is not a prime number it is divisible by {i}")
            break
    else:
        print(f"{num} is a prime number")

else:
    print(f"{num} is not a prime number")