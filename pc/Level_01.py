s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp." \
    " bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " \
    "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.  lmu ynnjw ml rfc spj."

alphabet = list("abcdefghijklmnopqrstuvwxyz")
alphabet_len = len(alphabet)

condition = {
    "k": "m",
    "o": "q",
    "e": "g",
}


def loop_index(length, current_pos):
    # Remember that len starts from 1, whereas current_pos starts from 0
    if current_pos >= length:
        return current_pos - length
    return current_pos


def replace(s):
    s_array = list(s)
    s_array_new = []
    replace_counter = 0

    for w in s_array:
        b = False

        for i in condition:
            if w == i:
                s_array_new.append(condition[i])
                b = True
                replace_counter += 1

        if not b:
            s_array_new.append(w)

    print("".join(s_array_new))
    print("Replace count: ", replace_counter)


def shift_letter(s, step):
    # Step is the amount of steps to shift the letter
    s_array = list(s)
    s_array_new = []

    for string_letter in s_array:
        b = False
        for i, alphabet_letter in enumerate(alphabet):
            if string_letter == alphabet_letter:
                s_array_new.append(alphabet[loop_index(alphabet_len, i + step)])
                b = True
                break
        # If no matches, then no shift needed
        if not b:
            s_array_new.append(string_letter)

    print("".join(s_array_new))

shift_letter(s, 2)

# Solution: ==================================================================================

print("".join(map(lambda x: x.isalpha() and chr((ord(x) + 2 - ord("a")) % 26 + ord("a")) or x, s)))
