# python3
import sys


def BWT(text):
    text_length = len(text)
    texts = []
    for i in range(text_length):
        texts.append(text[-i:] + text[:-i])
    texts = sorted(texts)
    return "".join([t[-1] for t in texts])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    # text = "qwerty$"
    print(BWT(text))