import numpy as np
first_word=input('ingresa una palabra significativa relacionada con economía (vacio para tomar una palabra al azar):  ')
gobierno=open("maquiavelo_el_principe.txt",encoding='UTF-8').read()

corpus=gobierno.split()

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield(corpus[i],corpus[i+1])

pairs=make_pairs(corpus)

word_dict={}

for word_1,word_2 in pairs: 
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1]=[word_2]

if first_word == '':
    first_word =np.random.choice(corpus)
print(first_word);
chain=[first_word]

n_words=100

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

print(' '.join(chain))


