# Daily Challenge #243 [Intermediate]: Fruit Basket

# Key takeaways:
# Shallow copying a list

import string

inp_fruit_dict = {
    'apple': 52,
    'banana': 32,
    'coconut': 155,
}
inp_fruit_dict2 = {
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
goal = 500
it = 0


def remove_duplicates(arr):
    return list(set(arr))


def array_loop(array, i, max_i, total, goal, prices, results):
    while total < goal:
        global it
        it += 1

        next_i = i + 1
        if next_i == max_i:
            pass
        else:
            new_array = array.copy()
            new_total = total
            array_loop(new_array, next_i, max_i, new_total, goal, prices, results)

        array[i] += 1
        total += prices[i]

        if total == goal:
            # print('success! ' + str(array))
            results.append(array)
            break
    else:
        pass


def program(fruit_dict):
    price_list = list(fruit_dict.values())
    total_fruit_types = len(price_list)

    quantity_list = [None] * total_fruit_types
    for i in range(total_fruit_types):
        quantity_list[i] = 0

    results = []

    array_loop(quantity_list, 0, total_fruit_types, 0, goal, price_list, results)

    for result in results:
        qp = [q * p for q, p in zip(result, price_list)]
        t = sum(qp)
        print(t)
    print(len(results))
    print(it)


program(inp_fruit_dict2)
