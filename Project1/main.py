import os, re, math
import time
from tqdm import tqdm

path = './enron1/spam/'
files = []
for r, d, f in os.walk(path):
    files.extend(f)
texts = []
for f in files:
    texts.append(open(path + f, 'r', encoding = "ISO-8859-1").read())

d = {}

for text in texts:
    for word in re.findall(r"[^\s]+", text):
        word = word.lower()
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

weights = []
for text in tqdm(texts[5:8]):
    weights.append([])
    list = [x.lower() for x in re.findall(r"[^\s]+", text)]
    for ddd in d:
        weights[-1].append(list.count(ddd) * math.log(len(d) / d[ddd]))

f = open('weights.txt','w')
f.write(str(weights))

# print({k: v for k, v in sorted(d.items(), key=lambda item: item[1])})

# for word in re.findall(r"[^\s]+", open('test/0046.2003-12-20.GP.spam.txt', 'r', encoding = "ISO-8859-1").read()):
#     if word in d:
#         print(word, d[word])
