# python3
import sys
from bisect import bisect_left

def BWT(text):
    text_length = len(text)
    texts = []
    for i in range(text_length):
        texts.append(text[-i:] + text[:-i])
    texts = sorted(texts)
    return "".join([t[-1] for t in texts])

def InverseBWT(bwt):
    # sorted_bwt = sorted(enumerate(bwt), key=lambda x: x[1])
    sorted_bwt = sorted(bwt)
    first_last = sorted(range(len(bwt)), key=bwt.__getitem__)
    temp = [None]*len(first_last)
    for num, value in enumerate(first_last):
        temp[value] = num
    first_last = temp
    res = []
    symbol = "$"
    symbol_position = 0
    while len(res) != len(bwt):
        res.append(symbol)
        symbol_position = first_last[symbol_position]
        symbol = sorted_bwt[symbol_position]


    return "".join(reversed(res))


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))