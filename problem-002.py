stop_val = 4_000_000

def fibonacci(goal_val):
    fib_sequence = [0,1]

    new_num = 0

    while new_num <= goal_val:
        prev_num        = fib_sequence[-1]
        prev_prev_num   = fib_sequence[-2]

        new_num         = prev_num + prev_prev_num

        fib_sequence.append(new_num)

    fib_sequence.pop()

    return fib_sequence


even_fib = []

for element in fibonacci(stop_val):
    if element % 2 == 0:
        even_fib.append(element)

print(sum(even_fib))










