# Daily Challenge #240 [Easy]: Typoglycemia

# Key takeaways:
# List comprehension
# The string.translate() function
# The random.sample() / .shuffle() function
# The string.punctuation set
# The regex to split string while preserving punctuations
# Trimming whitespaces

from random import sample
from string import punctuation
from re import findall


inp = """According to a research team at Cambridge University, it doesn't matter in what order the letters in a word are, 
        the only important thing is that the first and last letter be in the right place. 
        The rest can be a total mess and you can still read it without a problem.
        This is because the human mind does not read every letter by itself, but the word as a whole. 
        Such a condition is appropriately called Typoglycemia."""


def xform_typoglycemia(s):
    # w_list = s.translate(str.maketrans('', '', punctuation)).split(' ')
    w_list = findall(r"[\w']+|[.,!?;]", s)
    w_list_xformed = []

    for w in w_list:
        if w not in ['.', ',', '!', '?', ';'] and len(w) > 3:
            # Get characters
            s_char = w[0]
            m_chars = w[1:-1]
            e_char = w[-1]

            # Shuffle middle characters
            while True:
                m_chars_shuffled = ''.join(sample(list(m_chars), k=len(list(m_chars))))
                if m_chars_shuffled == m_chars:
                    continue
                else:
                    break

            # Re-join characters & append to new collection
            new_w = s_char + m_chars_shuffled + e_char
            w_list_xformed.append(new_w)
        else:
            w_list_xformed.append(w)
    return ''.join([' ' + w if w not in punctuation else w for w in w_list_xformed]).lstrip()


print(xform_typoglycemia(inp))
