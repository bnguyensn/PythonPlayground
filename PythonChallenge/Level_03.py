# Could improve..

with open("Level_03.txt", "r") as f:
    msg = "".join([line.rstrip() for line in f])
    msg_len = len(msg)
    check_range = 3  # Check 3 items to the left / right

    res = []
    counter = 0

    for i, character in enumerate(msg[check_range:msg_len - check_range:]):
        if character.islower():

            b = msg[i+check_range+1].isupper() and msg[i+check_range-1].isupper() and \
                msg[i+check_range+2].isupper() and msg[i+check_range-2].isupper() and \
                msg[i+check_range+3].isupper() and msg[i+check_range-3].isupper() and \
                msg[i+check_range+4].islower() and msg[i+check_range-4].islower()
            if b:
                counter += 1
                res.append(msg[i+check_range])

    print(counter)
    print(res)
