txt = open('les5task3.txt', 'r')
words = txt.read().lower().split()
print(dict(zip(words, list(map(lambda word: words.count(word), words)))))
txt.close()