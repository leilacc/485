import nltk
from nltk.corpus import wordnet as wn

if __name__ == '__main__':
    similarities = []
    with open('Miller-pairs', 'r') as pairs:
        for pair in pairs:
            words = pair.split()
            max_sim = 0
            for synset1 in wn.synsets(words[0], wn.NOUN):
                for synset2 in wn.synsets(words[1], wn.NOUN):
                    sim = wn.path_similarity(synset1, synset2)
                    max_sim = max(max_sim, sim)
            similarities.append(("%s-%s" % (words[0], words[1]), max_sim))
    sorted_similarities = sorted(similarities, key=lambda x: x[1])[::-1]
    for pair in sorted_similarities:
        print "%s %f" %(pair[0], pair[1])
