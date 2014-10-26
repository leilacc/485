preps = ['by', 'onto', 'toward', 'beside', 'for', 'among']
verbs = ['swam', 'hurried', 'placed', 'advanced','love', 'admire']
nouns = ['fish', 'whales', 'seals' ,'otters', 'we']

# Q2A
def add_unambig(word1, pp, count, unambiguous):
    pair = (word1, pp)
    if pair not in count:
        count[pair] = 1
        unambiguous.append(pair)
    else:
        count[pair] += 1

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

# Q2B
total_count_swam = 0
total_count_whales = 0
total_count_placed = 0
total_count_advanced = 0
n_verbs = 0
n_nouns = 0
with open('pp-corpus', 'r') as corpus:
    for line in corpus:
        words = line.split()
        for word in words:
            if word == "placed":
                total_count_placed += 1
            if word == "advanced":
                total_count_advanced += 1
            if word == "whales":
                total_count_whales += 1
            if word == "swam":
                total_count_swam += 1
            if word in verbs:
                n_verbs += 1
            if word in nouns:
                n_nouns += 1
print "total count swam: %d" % total_count_swam
print "total count whales: %d" % total_count_whales
print "total count advanced: %d" % total_count_advanced
print "total count placed: %d" % total_count_placed

print "total count of verbs: %d" % n_verbs
print "total count of nouns: %d" % n_nouns

extracted_swam = 0
extracted_whales = 0
extracted_placed = 0
extracted_advanced = 0
for pair, num in count.iteritems():
    if "placed" in pair:
        extracted_placed += num
    if "advanced" in pair:
        extracted_advanced += num
    if "swam" in pair:
        extracted_swam += num
    if "whales" in pair:
        extracted_whales += num
print "extracted count swam: %d" % extracted_swam
print "extracted count whales: %d" % extracted_whales
print "extracted count advanced: %d" % extracted_advanced
print "extracted count placed: %d" % extracted_placed

print "extracted count swam onto: %d" % count[("whales", "onto")]
print "extracted count whales onto: %d" % count[("swam", "onto")]
print "extracted count advanced for: %d" % count[("advanced", "for")]
