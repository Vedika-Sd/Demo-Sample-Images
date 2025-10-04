#sum all even numbers in list

num_list = []
for i in range(5):
    num = int(input("input numbers: "))
    num_list.append(num)

print("Input List: ", num_list)
sum = 0

for v in num_list:
    if v%2==0:
        sum = sum + v
        v+=1

print("Total Sum is ", sum)
