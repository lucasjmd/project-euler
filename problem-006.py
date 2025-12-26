nums = [x for x in range(1,101)]



def sum_squares(numbers: list) -> int:
    squared_nums = map(lambda num: pow(num,2), numbers)

    sum_of_squares = sum(squared_nums)

    return sum_of_squares


def squared_sums(numbers: list) -> int:
    square_of_sums = pow(sum(numbers),2)

    return square_of_sums

sum_of_squares = sum_squares(nums)
square_of_sums = squared_sums(nums)


difference = square_of_sums - sum_of_squares

print(difference)