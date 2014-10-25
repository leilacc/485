preps = ['by', 'onto', 'toward', 'beside', 'for', 'among']
verbs = ['swam', 'hurried', 'placed', 'advanced','love', 'admire']
nouns = ['seals' ,'otters', 'we']



unambiguous = []
potential_tuple = []
verb_state = 0
noun_state = 0
with open('pp-corpus', 'r') as corpus:
    for line in corpus:
        words = line.split()
        for word in words:
            if word in verbs and not verb_state:
                potential_tuple = [word]
                verb_state = 1
                noun_state = 0
            elif word in nouns and not noun_state:
                potential_tuple = [word]
                verb_state = 0
                noun_state = 1
            elif word in preps and (noun_state or verb_state):
                potential_tuple.append(word)
                unambiguous.append(potential_tuple)
                verb_state = 0
                noun_state = 0

print unambiguous
