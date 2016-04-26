from collections import Counter
import sys

def generate_ngrams(text, n):
    split_ngrams = zip(*[text[i:] for i in range(n)])
    return map(lambda x: ''.join(x), split_ngrams)


def ngram_stats(text, n):
    ngrams = []
    for w in text:
        ngrams.extend(generate_ngrams(w, n))
    return Counter(ngrams)


def main(text_path, c):
    text = None
    with open(text_path) as f:
        text = f.read().split()

    digrams = ngram_stats(text, 2)
    trigrams = ngram_stats(text, 3)
    print("\nDigrams: ")
    for n in digrams.most_common(c):
        print("({0}, {1})".format(n[1], n[0]))
    print("\nTrigrams: ")
    for n in trigrams.most_common(c):
        print("({0}, {1})".format(n[1], n[0]))


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
