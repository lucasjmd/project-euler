n = 191000

odd_sum = 0

for i in range(0,n+1):
    if (pow(i,2) % 2) == 1:
        odd_sum += pow(i,2)

print(odd_sum)