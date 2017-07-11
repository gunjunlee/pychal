import pickle
import urllib.request

fp = open('banner.p', 'rb')
text=pickle.load(fp)
print(text)

for i in text:
    for j in i:
        for k in range(0, j[1]):
            print('%s'%j[0], end='')
    print('')
