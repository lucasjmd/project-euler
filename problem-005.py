number = 1
prime_range = [2,3,5,7,11,13,17,19]
searching = True

while searching:
    print(f'{number}')
    for num in prime_range:
        if number % num == 0:
            continue

        else:
            number += 1
            break

    else:
        searching = False

print(number)
