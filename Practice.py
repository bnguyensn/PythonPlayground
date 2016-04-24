def digit_sum(n):
    total = 0
    for i in str(n):
        total += int(i)
    print(total)


def digit_sum2(n):
    total = 0
    while n // 10 > 0:
        total += n % 10
        n //= 10
    print(total)


def is_even(n):
    if n % 2 == 0:
        return True
    return False


def is_int(x):
    if x - round(x, 0) == 0:
        return True
    return False


def factorial(x):
    fact = 1
    while x > 0:
        fact *= x
        x -= 1
    return fact


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x - 1):
            if x % n == 0:
                return False
    return True


def reverse(text):
    reversed_letters = []
    for i in range(len(text)):
        reversed_letters.append(text[len(text) - 1 - i])
    return "".join(reversed_letters)


def anti_vowel(text):
    vowel_list = ["a", "e", "i", "o", "u"]
    no_vowel_text = ""
    for i in text:
        if not i.lower() in vowel_list:
            no_vowel_text += i
    return no_vowel_text


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scrabble_score(word):
    total = 0
    for i in word:
        total += score[i.lower()]
    return total


def censor(text, word):
    word_list = []
    word_start = 0
    censored_word = ""

    for i in range(len(word)):
        censored_word += "*"

    n = 0
    text += " "  # Quick hack
    for i in text:
        if i == " " or n == len(text) - 1:  # Another word has ended, or the sentence ended.
            this_word = text[word_start:n]
            print(this_word)
            if this_word == word:
                this_word = censored_word
            word_list.append(this_word)
            word_start = n + 1
        n += 1

    return " ".join(word_list)


def count(sequence, item):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == item:
            count += 1
    return count


def purify(numbers):  # Removes all odds
    purified_numbers = []
    for i in numbers:
        if i % 2 == 0:
            purified_numbers.append(i)
    return purified_numbers


def product(integers):
    product = 1
    for i in integers:
        product *= i
    return product


def remove_duplicates(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


def median(lst):
    list_length = len(lst)
    sorted_lst = sorted(lst)
    if is_even(list_length):
        return (sorted_lst[list_length // 2] + sorted_lst[(list_length // 2) - 1]) / 2
    else:
        return sorted_lst[(list_length - 1) // 2]


def fibonacci(lim):
    a, b = 0, 1
    while b < lim:
        print(b, end=", ")
        a, b = b, a + b
