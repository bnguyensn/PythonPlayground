# Daily Challenge #243 [Intermediate]: Fruit Basket

# Key takeaways:

import string

inp_fruit_dict = {
    'apple': 52,
    'banana': 32,
    'coconut': 155,
}
inp_fruit_dict2 = {
    'apple': 52,
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
inp_target_budget = 500


def fruit_loop(fruit_dict, target_budget, current_budget, current_chain):
    for fruit, price in fruit_dict.items():
        new_current_budget = current_budget + price
        if new_current_budget > target_budget:
            break
        else:
            if fruit in current_chain:
                current_chain[fruit] += 1
            else:
                current_chain[fruit] = 0
            if new_current_budget == target_budget:
                pass
            else:
                fruit_loop(fruit_dict, target_budget, new_current_budget, current_chain)


fruit_loop(inp_fruit_dict, inp_target_budget, 0, {})
