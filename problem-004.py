current_max_factors = [None, None]

for factor_1 in range(100,1000):
    for factor_2 in range(100,1000):

        product = factor_1 * factor_2

        product = list(str(product))

        digits_in_product = len(product)

        number_range = len(product)//2

        for i in range(number_range):
            if product[i] == product.pop():
                continue
            else:
                break

        else:
            current_max_factors[0] = factor_1
            current_max_factors[1] = factor_2

print(current_max_factors)
print(current_max_factors[0]*current_max_factors[1])