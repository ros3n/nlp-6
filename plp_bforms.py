import pickle
import imp
import sys


def plp_bforms(PLP, inp=sys.stdin):
    data = inp.read()
    data = data.split()
    p = PLP()
    ids = []
    nids = []
    for w in data:
        i = plp_id(w, p)
        ids.append(i) if i else nids.append(w)
    bforms = [p.bform(i) for i in ids]
    bforms.extend(nids)
    return bforms


def plp_id(word, plp):
    rec = plp.rec(word)
    return rec[0] if rec else None


def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')

    plp = imp.load_source('plp', '/usr/local/plp/plp.py')
    data = plp_bforms(plp.PLP)
    with open('/home/pjn2016/rrozak/forms.data', 'wb') as f:
        pickle.dump(data, f)

if __name__ == '__main__':
    main()
