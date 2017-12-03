# Daily Challenge #243 [Intermediate]: Fruit Basket

# Key takeaways:
# Fruit basket recursive looping problem
# Performance measurement
# Create an array filled with zeroes of X length
# Shallow copying a list
# String formatting: decimal places

import time  # Performance measurement

inp_fruit_dict = {
    'apple': 59,
    'banana': 32,
    'coconut': 155,
    'grapefruit': 128,
    'jackfruit': 1100,
    'kiwi': 41,
    'lemon': 70,
    'mango': 97,
    'orange': 73,
    'papaya': 254,
    'pear': 37,
    'pineapple': 399,
    'watermelon': 500
}
inp_goal = 500


def array_loop(array, i, max_i, total, goal, prices, results):
    while total < goal:

        next_i = i + 1
        if next_i == max_i:
            pass
        else:
            new_array = array.copy()
            array_loop(new_array, next_i, max_i, total, goal, prices, results)

        array[i] += 1
        total += prices[i]

        if total == goal:
            results.append(array)
            break


def process_results(quantity_list, fruit_list):
    result_str = ''

    for i in range(len(quantity_list)):
        if quantity_list[i] > 0:
            # Inflection
            fruit_name = fruit_list[i] + 's' if quantity_list[i] > 1 else fruit_list[i]
            # Add fruit to result string
            result_str = result_str + str(quantity_list[i]) + ' ' + fruit_name + ', '

    return result_str.rstrip(', ')


def program(fruit_dict):
    # Separate the fruit dictionary into a fruit array and price array
    # We do this because copying array is faster than copying dictionary
    fruit_list = list(fruit_dict.keys())
    price_list = list(fruit_dict.values())
    total_fruit_types = len(price_list)

    # Empty array to store final answers, in quantity arrays and strings
    result_arrays = []
    result_strs = []

    # Create an initial all-zero array with length = total fruit types
    initial_quantity_list = [None] * total_fruit_types
    for i in range(total_fruit_types):
        initial_quantity_list[i] = 0

    # THE MAGICAL RECURSIVE FUNCTION
    array_loop(initial_quantity_list, 0, total_fruit_types, 0, inp_goal, price_list, result_arrays)

    # Turn result arrays into strings
    for result_array in result_arrays:
        result_strs.append(process_results(result_array, fruit_list))

    # Display results
    print('\n'.join(result_strs))
    print('Total possible combinations found: ' + str(len(result_arrays)))

    """
    # Optional function to check whether results are correct [LIST COMPREHENSION]
    for result in result_arrays:
        qp = [q * p for q, p in zip(result, price_list)]
        total = sum(qp)
        print(total)
    """


t = time.perf_counter()  # Performance measurement
program(inp_fruit_dict)
print('Time taken {0:.4f}s'.format((time.perf_counter() - t)))  # Performance measurement
