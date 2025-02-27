from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

global file_path
file_path = "news_sample.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()
print(len(text))

# Tokenisering af sætning
tokens = word_tokenize(text)
print(len(tokens))

ps = PorterStemmer()
stemmed_tokens = [ps.stem(w) for w in tokens]
print(len(stemmed_tokens))

# Hent stopord
stop_words = set(stopwords.words('english'))

# Fjern stopord
filtered_tokens = [w for w in stemmed_tokens if w.lower() not in stop_words]
print(len(filtered_tokens))
