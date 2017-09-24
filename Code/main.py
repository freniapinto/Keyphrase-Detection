import argparse
from .graph import GraphApproach
from .tfidf import TfidfApproach


def tfidf():
    t = TfidfApproach()
    t.run()

def graph():
    g= GraphApproach()
    g.run()

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparser(help='Choose the technique to perform keyphrase detection')

    tfidf_parser = sub_parser.add_parser('tfidf',help='tfidf technique')
    tfidf_parser.set_defaults(func=tfidf)

    graph_parser = sub_parser.add_parser('graph',help='graph technique')
    graph_parser.set_defaults(func=graph)

    args = parser.parse_args()

    args.func()
