n = int(input("Enter n: "))
sum = 0
if n > 0:
    for i in range(n):
        a = int(input())
        if(a == 0):
            sum += 1
print(sum)
