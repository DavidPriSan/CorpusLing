import nltk, re, string, collections, json, kaggle, sys
from nltk.util import ngrams

#Autenticacion Kaggle API
#kaggle.api.authenticate()

#Descarga dataset
#kaggle.api.dataset_download_files('rtatman/120-million-word-spanish-corpus', path='./src/data/', unzip=True)

#Carga y formateo de datos
with open ("./src/data/spanishText_110000_115000", "r", encoding="latin-1") as file:
    text = file.read()
    
text = text.lower()

text = re.sub('<.*>', '', text)

text = re.sub('ENDOFARTICLE.', '', text)

punctuationNoPeriod = "[" + re.sub(r"\.", "", string.punctuation) + "]"
text = re.sub(punctuationNoPeriod, " ", text)

text = re.sub(r"\d+", "", text)

#Palabras individuales
tokenized = text.split()

#Bigramas (ya en json)
bigrams = [{} for i in range(len(tokenized))]
i = 0
for j in tokenized:
	if i < len(tokenized)-1:
		bigrams[i] = {"word": j, "bigram": tokenized[i + 1]}
		i += 1
	else:
		bigrams[i] = {"word": j, "bigram": ""}
		i += 1

#Devolver resultado en json
json.dump(bigrams, sys.stdout)