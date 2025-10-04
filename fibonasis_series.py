n1 = 0
n2 = 1

term = int(input("Enter number of terms to print fibonasis series: "))

while(term>0):
    n3 = n1+n2
    print(n1)
    n1 = n2
    n2 = n3
    term -=1