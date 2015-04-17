import nltk

file_content = open("sample.txt").read()
tokens = nltk.word_tokenize(file_content)
print tokens

entries = nltk.corpus.cmudict.entries()
print len(entries)

for token in tokens:
    for entry in entries:
        if token == entry[0]:
            print entry