from collections import Counter
import pickle
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def plp_stats(data):
    return Counter(data).most_common()


def load_data(path):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    data = None
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data


def zipf(x, k):
    return k / (x + 1)


def mandelbrot(x, p, d, b):
    return p / (((x + 1) + d) ** b)


def fit(func, xdata, ydata):
    popt, pcov = curve_fit(func, xdata, ydata)
    return popt


def plot_func(func, xdata, color):
    plt.plot(xdata, func, color)


def hapax_legomena(stats):
    return map(lambda x: x[0], filter(lambda x: x[1] == 1, stats))

def half_of_text(stats, size):
    counter = 0
    res = []
    for s in stats:
        res.append(s[0])
        counter += s[1]
        if counter >= size:
            break
    return res


def plot_stats(frequencies, ranks):
    plot_func(map(lambda x: frequencies[x], ranks), ranks, 'r')

    zopt = fit(zipf, ranks, frequencies)
    plot_func(map(lambda x: zipf(x, zopt[0]), ranks), ranks, 'g')

    mopt = fit(mandelbrot, ranks, frequencies)
    plot_func(map(lambda x: mandelbrot(x, mopt[0], mopt[1], mopt[2]), ranks), ranks, 'b')


def main(forms_path):
    data = load_data(forms_path)
    stats = plp_stats(data)
    frequencies = np.array(map(lambda x: x[1], stats))
    ranks = np.array(range(len(frequencies)))

    size = len(frequencies)

    hl = hapax_legomena(stats)
    print 'Hapax legomena ({0}/{1}):'.format(len(hl), size)
    for w in hl:
        print w,

    print "\n\n"

    p50 = half_of_text(stats, sum(frequencies) / 2)
    print '50% ({0}/{1}):'.format(len(p50), size)
    for w in p50:
        print w,

    raw_input()

    plot_stats(frequencies, ranks)
    plt.show()


if __name__ == '__main__':
    main(sys.argv[1])
