from nltk import word_tokenize, sent_tokenize
from nltk import pos_tag_sents
from nltk.chunk.regexp import RegexpParser
from nltk.chunk import tree2conlltags
from nltk.corpus import stopwords
import glob
import re
from itertools import chain, groupby

stop_words = set(stopwords.words('english'))

def extract_keyphrases(texts,content,method='phrase'):
    candidate_dict = {}
    for text in texts:
        vocabulary = generate_candidate(text, method=method)
        candidate_dict[text] = vocabulary
    return candidate_dict

def removeNonAscii(s):
    return "".join(i for i in s if ord(i)<128)

def generate_candidate(texts, method='word', remove_punctuation=False):
    words_ = []
    candidates = []
    sentences = sent_tokenize(texts)
    for each in sentences:
        words = word_tokenize(each)
        words = list(map(lambda s: s.lower(), words))
        words_.append(words)
    tagged_words = pos_tag_sents(words_)
    if method == 'word':
        tags = set(['JJ', 'JJR', 'JJS', 'NN', 'NNP', 'NNS', 'NNPS'])
        tagged_words = chain.from_iterable(tagged_words)
        for word, tag in tagged_words:
            if tag in tags and word.lower() not in stop_words:
                candidates.append(word)
    else:
        grammar = r'KT: {(<JJ>* <NN.*>+ <IN>)? <JJ>* <NN.*>+}'
        chunker = RegexpParser(grammar)
        all_tag = chain.from_iterable([tree2conlltags(chunker.parse(tag)) for tag in tagged_words])
        for key, group in groupby(all_tag, lambda tag: tag[2] != 'O'):
            candidate = ' '.join([word for (word, pos, chunk) in group])
            if key is True and candidate not in stop_words:
                candidates.append(candidate)
    return candidates

def clean():
    content ={}
    keyphrases_dict = {}
    text =[]
    filenames = []
    for filename in glob.glob('./src/corpus/*.txt'):
        content_f = open(filename)
        temp = content_f.read()
        try:
            clean_corpus = temp[temp.lower().index("abstract")+len("abstract"):temp.lower().index("introduction")]
        except ValueError:
            clean_corpus = temp[temp.lower().index("abstract")+len("abstract"):temp.lower().index("background")]
        clean_corpus = clean_corpus.replace('\n'," ")
        clean_corpus = re.sub("\[[0-9]+\]"," ",clean_corpus)
        clean_corpus = re.sub("\([0-9]+\)"," ",clean_corpus)
        clean_corpus = removeNonAscii(clean_corpus)
        punctuation=['!', '@', '#', '$', '^', '&', '*', '(', ')', '_', '+', '=', '{', '[', '}', ']', '|','\\', '"', "'", ';', '/', '<', '>', '?', '%',':']
        for each in punctuation:
            clean_corpus = clean_corpus.replace(each,'')
        content[filename] = clean_corpus
    for each in content:
        text.append(content[each])
        filenames.append(each)
    keyphrases = extract_keyphrases(text,content)
    return keyphrases
