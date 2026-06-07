import sys
import re


def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    first_line = input_data[0].split()
    n = int(first_line[0])
    m = int(first_line[1])

    dict_words = set()
    for i in range(1, n + 1):
        dict_words.add(input_data[i].strip().lower())

    text_lines = input_data[n + 1: n + 1 + m]
    text = " ".join(text_lines)

    text_words = re.findall(r"[a-zA-Z]+", text)

    text_words_lower = set()
    has_unknown = False

    for word in text_words:
        w_low = word.lower()
        text_words_lower.add(w_low)
        if w_low not in dict_words:
            has_unknown = True

    if has_unknown:
        print("Some words from the text are unknown.")
    elif len(dict_words) > len(text_words_lower):
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")


if __name__ == '__main__':
    solve()