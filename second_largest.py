n = int(input("Enter number of elements in list: "))
numbers = []

for a in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Input list = ", numbers)

sorted_list = numbers.sort()

print(f"Second largest number is {numbers[n-2]}")        # array indexing starts from 0 thus require to minus 2