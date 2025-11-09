import pymorphy3
import nltk
import re
    
morph = pymorphy3.MorphAnalyzer()

with open('lab1/text.txt', 'r', encoding='utf-8') as file:
    t = file.read()

t = re.sub(r"[^а-яА-Я\. ]", " ", t)
t = re.sub(r'\s+', ' ', t)

def f(w1, w2):
    res_w1 = morph.parse(w1)[0]
    res_w2 = morph.parse(w2)[0]
    if any(tag.POS in ['NOUN', 'ADJF', 'ADJS'] for tag in [res_w1.tag, res_w2.tag]) and all(getattr(res_w1.tag, i, '1') == getattr(res_w2.tag, i, '0') for i in ['case', 'gender', 'number']):
        return {'input' : (w1, w2), 'res' : (res_w1.normal_form, res_w2.normal_form)}
    return {}

words = t.split(' ')
res = [f(words[i], words[i+1]) for i in range(len(words)-1) if words[i+1][-1] != '.' and words[i][-1] !='.']

for d in res:
    if d:
        print('Входные два слова: ', *d['input'])
        print('Результат: ', *d['res'])
