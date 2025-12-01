import gensim

pos = ["игра_NOUN", "шахматист_NOUN", "пат_NOUN","сочетание_NOUN"]
neg = []
word2vec = gensim.models.KeyedVectors.load_word2vec_format("lab2/cbow.txt", binary=False)
d = word2vec.most_similar(positive=pos, negative=neg)
for i in d[:10]:
    if 'комбинация_NOUN' == i[0] or 'игрок_NOUN' == i[0]:
        print(f'{i[0]} есть в топ-10')
print('Топ-10 слов')
print(*d[:10], sep='\n')
