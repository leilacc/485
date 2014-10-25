def add_unambig(word1, pp, count, unambiguous):
    pair = (word1, pp)
    if pair not in count:
        count[pair] = 1
        unambiguous.append(pair)
    else:
        count[pair] += 1

preps = ['by', 'onto', 'toward', 'beside', 'for', 'among']
verbs = ['swam', 'hurried', 'placed', 'advanced','love', 'admire']
nouns = ['fish', 'whales', 'seals' ,'otters', 'we']

unambiguous = []
count = {}
with open('pp-corpus', 'r') as corpus:
    for line in corpus:
        words = line.split()
        for i, word in enumerate(words):
            if word in preps:
                for j in [1, 2]:
                    new_index = i - j
                    if new_index < 0:
                        break
                    if words[new_index] in verbs and words[i - 1] not in nouns:
                        add_unambig(words[new_index], word, count, unambiguous)
                        print "%s %s %s" % (words[new_index], words[i - 1], word)
                        break
                    elif words[new_index] in nouns and words[i - 2] not in verbs:
                        add_unambig(words[new_index], word, count, unambiguous)
                        print "%s %s %s" % (words[new_index], words[i - 1], word)
                        break




for pair in unambiguous:
    print "%d %s %s" % (count[tuple(pair)], pair[0], pair[1])
