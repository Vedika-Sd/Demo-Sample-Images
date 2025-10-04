#Find largest number

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# print(f"Largest number in {a}, {b}, {c} is {max(a,b,c)}")

#To take multiple inputs at time
n = int(input("Enter how many number you want to compare: "))
numbers = []   #define list similar to array in c
for a in range(n):
    num = float(input(f"Enter number {a+1}: "))
    numbers.append(num)
    
largest = max(numbers)
print(f"Largest number is {largest}")





