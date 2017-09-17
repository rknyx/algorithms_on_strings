# python3
import sys


def sort_characters(text):
    counts = [0] * 5
    order = [None] * len(text)
    letter_to_index = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}
    # letter_to_index = {'$': 0, 'a': 1, 'b': 2}
    for char in text:
        counts[letter_to_index[char]] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    for i in reversed(range(len(text))):
        letter_index = letter_to_index[text[i]]
        counts[letter_index] -= 1
        order[counts[letter_index]] = i
    return order


def compute_char_classes(order, text):
    classes = [None] * len(text)
    last_class, prev_symbol = -1, '-'
    for order_value in order:
        symbol = text[order_value]
        if symbol != prev_symbol:
            prev_symbol = symbol
            last_class += 1
        classes[order_value] = last_class
    return classes


def sort_doubled(S, L, order, classes):
    new_order = [None] * S
    count = [0] * S
    for i in classes:
        count[i] += 1
    for i in range(1, len(classes)):
        count[i] += count[i-1]
    for i in reversed(range(S)):
        start = (order[i] - L + S) % S
        clazz = classes[start]
        count[clazz] -= 1
        new_order[count[clazz]] = start
    return new_order


def update_classes(new_order, classes, L):
    order_len = len(new_order)
    new_classes = [None] * order_len
    last_class_left, last_class_right = -1, -1
    classes_counter = -1
    for order_value in new_order:
        left_index = order_value
        right_index = (left_index + L) % order_len
        if classes[right_index] != last_class_right or classes[left_index] != last_class_left:
            classes_counter += 1
            new_classes[left_index] = classes_counter
            last_class_right = classes[right_index]
            last_class_left = classes[left_index]
        else:
            new_classes[left_index] = classes_counter
    return new_classes


def build_suffix_array(text):
    order = []
    text_length = len(text)
    order = sort_characters(text)
    classes = compute_char_classes(order, text)

    L = 1
    while L < text_length:
        order = sort_doubled(text_length, L, order, classes)
        classes = update_classes(order, classes, L)
        L *= 2
    return order


def test_sort_chars():
    orig_text = "acgtacgtacgt$"
    sorted_text = sort_characters(orig_text)
    print(sorted_text)


def test_compute_char_classes():
    orig_text = "acgtacgtacgt$"
    order = sort_characters(orig_text)
    classes = compute_char_classes(order, orig_text)
    print(sorted_text)

if __name__ == '__main__':
    # test_compute_char_classes()
    # text = sys.stdin.readline().strip()
    text = "AACGATAGCGGTAGA$"
    print(" ".join(map(str, build_suffix_array(text))))
