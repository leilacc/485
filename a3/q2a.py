preps = ['by', 'onto', 'toward', 'beside', 'for', 'among']
verbs = ['swam', 'hurried', 'placed', 'advanced','love', 'admire']
nouns = ['fish', 'whales', 'seals' ,'otters', 'we']

unambiguous = []
count = {}
with open('pp-corpus', 'r') as corpus:
    for line in corpus:
        words = line.split()
        for i, word in enumerate(words):
            if (word in verbs or word in nouns) and (
                i + 1 < len(words) and words[i + 1] in preps):
                pair = (word, words[i + 1])
                if pair not in count:
                    count[pair] = 1
                    unambiguous.append(pair)
                else:
                    count[pair] += 1

for pair in unambiguous:
    print "%d %s %s" % (count[tuple(pair)], pair[0], pair[1])
