#Load Data

filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()


#split text by White Space 

words = text.split()
print(words[:100])

print("==============================================================")

#split by words

import re
words1 = re.split(r'\W+', text)
print(words1[:100])

print("==============================================================")

#split text by whitespace and remove punctuation from each word

import string 
table = str.maketrans('','', string.punctuation)
stripped_text = [w.translate(table) for w in words]
print(stripped_text[:100])

print("==============================================================")

#convert to lower case

words = [word.lower() for word in words]
print(words[:100])

print("==============================================================")

#cleaning text using nltk (Natural Language Toolkit)

#tokenixation 

import nltk
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
print(tokens[:100])

print("==============================================================")

#remove all token which ar not alphabatic

words2 = [word for word in tokens if word.isalpha()]
print(words2[:100])

print("==============================================================")

#filter out stopword 
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print(stop_words)

print("==============================================================")

words3 = [w for w in words if not w in stop_words]
print(words[:100])

print("==============================================================")

#stemming of words

from nltk.stem.porter import PorterStemmer

porter = PorterStemmer()
stemmed = [porter.stem(word) for word in tokens]
print(stemmed[:100])

