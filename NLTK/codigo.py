from nltk.corpus import stopwords
from nltk.corpus import wordnet

print('\nEjercicio 1')

#Seleccionamos el lenguaje en el que queremos que funcione nuestro stopwords
stoplist = stopwords.words('english')

#Texto que queremos limpiar
text = '''
In computing, stop words are words which are filtered out before or after 
processing of natural language data (text). Though "stop words" usually 
refers to the most common words in a language, there is no single universal 
list of stop words used by all natural language processing tools, and 
indeed not all tools even use such a list. Some tools specifically avoid 
removing these stop words to support phrase search.
'''
#Imprimimos el texto original
print("\nTexto original")
print(text)

#Listas por comprension MUY IMPORTANTE
#.split() divide el texto en palabras separadas
#solo se guardan las palabras si no estan en la stoplist anteriormente creada (if word NOT IN stoplist
clean_word_list = [word for word in text.split() if word not in stoplist]
print("\nDespués de remover las stop words del texto")
#imprimimos las palabras con las que nos quedamos (las limpias)
print(clean_word_list)

print('\nEjercicio 2')

from nltk.tokenize import TweetTokenizer
#Inicializamos el tokenizador de tweets
tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
#Es el texto del tweet
tweet_text = "NoSQL introduction - w3resource http://bit.ly/1ngHC5F  #nosql #database #webdev"
print("\nOriginal Tweet:")
print(tweet_text)
#tokenizamos las palabras del tweet(las separamos
result = tknzr.tokenize(tweet_text)
#Imprimimos
print("\nTokenize a twitter text:")
print(result)

print('\nEjercicio 3')

from nltk.tokenize import sent_tokenize, word_tokenize
#Texto que queremos tokenizar
text = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."
#Imprimimos el texto original
print("\nOriginal string:")
print(text)
#Tokenizamos haciendo una lista por comprension, pero por frases, separando 
print("\nTokenize words sentence wise:")
result = [word_tokenize(t) for t in sent_tokenize(text)]
print("\nRead the list:")
for s in result:
    print(s)


print('\nEjercicio 4')

def analyse_word(word):

    syns = wordnet.synsets(word)
    for word in syns:
        print("\nDefination of", word)
        print(word.definition())
        print("\nExamples of", word)
        print(word.examples())


analyse_word("battle")
analyse_word("love")
analyse_word("sports")
analyse_word("table")
