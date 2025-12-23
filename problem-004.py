current_max_factors = [None, None]
biggest_palindrome = 0

for factor_1 in range(100,1000):
    for factor_2 in range(100,1000):

        product_int = factor_1 * factor_2

        product_list = list(str(product_int))

        digits_in_product = len(product_list)

        number_range = len(product_list)//2 # Unneccessary but adds clarity

        if product_int > biggest_palindrome:
            for i in range(number_range):
                if product_list[i] == product_list.pop():
                    continue
                else:
                    break

            else:
                if product_int > biggest_palindrome:
                    current_max_factors[0] = factor_1
                    current_max_factors[1] = factor_2
                    biggest_palindrome = product_int


print(current_max_factors)
print(current_max_factors[0]*current_max_factors[1])