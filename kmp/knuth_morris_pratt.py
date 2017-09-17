# python3
import sys
from array import array

global prefix_function_values


def prefix_function(text):
    res = [0] * len(text)
    border = 0
    for i in range(1, len(text)):
        while border > 0 and text[border] != text[i]:
            border = res[border - 1]
        if text[border] == text[i]:
            border += 1
        else:
            border = 0
        res[i] = border
    return res


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    result = []
    pattern_len = len(pattern)
    d_pattern_len = 2 * pattern_len
    if pattern_len > len(text):
        return []

    new_string = pattern + "$" + text
    prefix_function_res = prefix_function(new_string)
    return [x - d_pattern_len for (x, y) in filter(lambda x: x[1] == pattern_len, enumerate(prefix_function_res))]


if __name__ == '__main__':
    # pattern = "ATAT"
    # text = "GATATATGCATATACTT"
    # result = find_pattern(pattern, text)
    # print(" ".join(map(str, result)))

    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()

    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))


