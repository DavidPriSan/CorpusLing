import nltk, re, string, collections, json, kaggle, sys
from nltk.util import ngrams

#Autenticacion Kaggle API
#kaggle.api.authenticate()

#Descarga dataset
#kaggle.api.dataset_download_files('rtatman/120-million-word-spanish-corpus', path='./src/data/', unzip=True)

#Carga y formateo de datos
with open ("./src/data/spanishText_10000_15000", "r", encoding="latin-1") as file:
    text = file.read()
    
text = re.sub('<.*>', '', text)

text = re.sub('ENDOFARTICLE.', '', text)

punctuationNoPeriod = "[" + re.sub(r"\.", "", string.punctuation) + "]"
text = re.sub(punctuationNoPeriod, "", text)

tokenized = text.split()

#Conteo
def conteo(a):
	dic = {}
	for j in a:
		if j in dic:
			dic[j] += 1
		else:
			dic[j] = 1
	return dic

counted = conteo(tokenized)
jsoned = [{} for i in range(len(counted))]
i = 0
for j in counted:
	jsoned[i] = {"word": j, "count": counted[j]}
	i += 1

#Devolver resultado en json
json.dump(jsoned, sys.stdout)