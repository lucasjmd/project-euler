n = 1000

multiples_sum = 0

valid_multiples = []

for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0:
        valid_multiples.append(i)

for i in valid_multiples:
    multiples_sum += i

print(multiples_sum)

