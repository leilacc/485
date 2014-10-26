import nltk
from nltk.corpus import wordnet as wn

if __name__ == '__main__':
    with open('Miller-pairs', 'r') as pairs:
        for pair in pairs:
            words = pair.split()
            max_sim = 0
            for synset1 in wn.synsets(words[0], wn.NOUN):
                for synset2 in wn.synsets(words[1], wn.NOUN):
                    sim = synset1.path_similarity(synset2)
                    max_sim = max(max_sim, sim)
            print("path_similarity of %s and %s: %f" % (words[0], words[1], max_sim))
